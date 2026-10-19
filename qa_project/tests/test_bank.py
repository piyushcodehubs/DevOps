"""Unit/integration tests: Bank working together with Account."""
import pytest

from app.account import Account
from app.bank import AccountNotFoundError, Bank


@pytest.fixture
def bank():
    b = Bank()
    b.add_account(Account("Ravi", 100))
    b.add_account(Account("Anita", 50))
    return b


def test_find_returns_the_right_account(bank):
    assert bank.find("Ravi").balance == 100


def test_find_ignores_case_and_spaces(bank):
    assert bank.find("  ravi ").owner == "Ravi"


def test_find_slow_and_find_agree(bank):
    assert bank.find_slow("Anita") is bank.find("Anita")


def test_duplicate_owner_is_rejected(bank):
    with pytest.raises(ValueError, match="already exists"):
        bank.add_account(Account("RAVI"))
    assert len(bank) == 2


def test_unknown_owner_raises(bank):
    with pytest.raises(AccountNotFoundError):
        bank.find("Nobody")
    with pytest.raises(AccountNotFoundError):
        bank.find_slow("Nobody")


def test_transfer_moves_money(bank):
    bank.transfer("Ravi", "Anita", 30)
    assert bank.find("Ravi").balance == 70
    assert bank.find("Anita").balance == 80


def test_transfer_keeps_total_constant(bank):
    before = bank.total_deposits()
    bank.transfer("Ravi", "Anita", 30)
    assert bank.total_deposits() == before


def test_failed_transfer_changes_nothing(bank):
    with pytest.raises(ValueError, match="Insufficient"):
        bank.transfer("Anita", "Ravi", 500)
    assert bank.find("Ravi").balance == 100
    assert bank.find("Anita").balance == 50


def test_transfer_to_unknown_account_changes_nothing(bank):
    with pytest.raises(AccountNotFoundError):
        bank.transfer("Ravi", "Nobody", 10)
    assert bank.find("Ravi").balance == 100


def test_transfer_to_same_account_is_rejected(bank):
    with pytest.raises(ValueError, match="same account"):
        bank.transfer("Ravi", "ravi", 10)
    assert bank.find("Ravi").balance == 100


def test_total_deposits(bank):
    assert bank.total_deposits() == 150
