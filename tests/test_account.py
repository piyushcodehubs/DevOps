"""Unit tests: the Account class on its own (normal behaviour)."""
import pytest

from app.account import Account


def test_new_account_defaults_to_zero_balance():
    assert Account("Ravi").balance == 0


def test_new_account_keeps_owner_and_opening_balance():
    acc = Account("Ravi", 100)
    assert acc.owner == "Ravi"
    assert acc.balance == 100


def test_owner_name_is_trimmed():
    assert Account("  Ravi  ").owner == "Ravi"


def test_deposit_increases_balance():
    acc = Account("Ravi", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw_decreases_balance():
    acc = Account("Ravi", 100)
    acc.withdraw(40)
    assert acc.balance == 60


def test_withdraw_exact_balance_leaves_zero():
    acc = Account("Ravi", 100)
    acc.withdraw(100)
    assert acc.balance == 0


def test_withdraw_more_than_balance_raises_and_keeps_balance():
    acc = Account("Ravi", 100)
    with pytest.raises(ValueError, match="Insufficient"):
        acc.withdraw(500)
    assert acc.balance == 100


def test_sequence_of_operations():
    acc = Account("Ravi")
    acc.deposit(200)
    acc.withdraw(75)
    acc.deposit(25)
    assert acc.balance == 150
