"""Integration tests: Account + Bank + storage working together."""
import pytest

from app.account import Account
from app.bank import Bank
from app.storage import load_account, save_account


def test_save_and_load_roundtrip(tmp_path):
    path = tmp_path / "acc.json"
    acc = Account("Ravi", 100)
    acc.deposit(25)
    save_account(acc, path)

    loaded = load_account(path)
    assert loaded.owner == "Ravi"
    assert loaded.balance == 125


def test_loaded_account_is_still_usable(tmp_path):
    path = tmp_path / "acc.json"
    save_account(Account("Ravi", 100), path)

    loaded = load_account(path)
    loaded.withdraw(40)
    assert loaded.balance == 60


def test_unicode_owner_survives_roundtrip(tmp_path):
    path = tmp_path / "acc.json"
    save_account(Account("रवि कुमार", 10), path)
    assert load_account(path).owner == "रवि कुमार"


def test_transfer_then_persist_then_reload(tmp_path):
    bank = Bank()
    bank.add_account(Account("Ravi", 100))
    bank.add_account(Account("Anita", 50))
    bank.transfer("Ravi", "Anita", 30)

    save_account(bank.find("Ravi"), tmp_path / "ravi.json")
    save_account(bank.find("Anita"), tmp_path / "anita.json")

    reloaded = Bank()
    reloaded.add_account(load_account(tmp_path / "ravi.json"))
    reloaded.add_account(load_account(tmp_path / "anita.json"))
    assert reloaded.find("Ravi").balance == 70
    assert reloaded.find("Anita").balance == 80
    assert reloaded.total_deposits() == 150


def test_loading_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_account(tmp_path / "does_not_exist.json")


def test_loading_corrupted_file_raises_value_error(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("this is not json", encoding="utf-8")
    with pytest.raises(ValueError):
        load_account(path)


def test_loading_file_with_missing_field_raises(tmp_path):
    path = tmp_path / "partial.json"
    path.write_text('{"owner": "Ravi"}', encoding="utf-8")
    with pytest.raises(ValueError, match="Missing field"):
        load_account(path)


def test_loading_file_with_invalid_data_raises(tmp_path):
    path = tmp_path / "negative.json"
    path.write_text('{"owner": "Ravi", "balance": -5}', encoding="utf-8")
    with pytest.raises(ValueError):
        load_account(path)
