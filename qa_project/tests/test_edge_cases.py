"""Edge cases and error handling: bad, odd, extreme input."""
import pytest

from app.account import Account


@pytest.mark.parametrize("bad_owner", ["", "   ", None, 123])
def test_invalid_owner_is_rejected(bad_owner):
    with pytest.raises(ValueError, match="Owner"):
        Account(bad_owner)


def test_negative_opening_balance_is_rejected():
    with pytest.raises(ValueError):
        Account("Ravi", -1)


def test_non_numeric_opening_balance_is_rejected():
    with pytest.raises(TypeError):
        Account("Ravi", "100")


@pytest.mark.parametrize("amount", [0, -1, -0.01])
def test_non_positive_amounts_are_rejected(amount):
    acc = Account("Ravi", 100)
    with pytest.raises(ValueError, match="positive"):
        acc.deposit(amount)
    with pytest.raises(ValueError, match="positive"):
        acc.withdraw(amount)
    assert acc.balance == 100


@pytest.mark.parametrize("amount", ["abc", "50", None, [10], True])
def test_wrong_type_amounts_are_rejected(amount):
    acc = Account("Ravi", 100)
    with pytest.raises(TypeError):
        acc.deposit(amount)
    with pytest.raises(TypeError):
        acc.withdraw(amount)
    assert acc.balance == 100


@pytest.mark.parametrize("amount", [float("nan"), float("inf"), float("-inf")])
def test_nan_and_infinity_are_rejected(amount):
    acc = Account("Ravi", 100)
    with pytest.raises(ValueError, match="finite"):
        acc.deposit(amount)
    assert acc.balance == 100


def test_huge_amount_is_handled():
    acc = Account("Ravi")
    acc.deposit(10**12)
    assert acc.balance == 10**12


def test_floating_point_amounts_need_approx():
    # 0.1 + 0.2 is 0.30000000000000004 in floating point, so compare with approx.
    acc = Account("Ravi")
    acc.deposit(0.1)
    acc.deposit(0.2)
    assert acc.balance == pytest.approx(0.3)


def test_very_small_positive_amount_is_allowed():
    acc = Account("Ravi", 1)
    acc.withdraw(0.01)
    assert acc.balance == pytest.approx(0.99)
