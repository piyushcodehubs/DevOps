"""Account model with input validation."""
import math


def _validate_amount(amount):
    """Raise if amount is not a positive, finite number."""
    # bool is a subclass of int in Python, so reject it explicitly.
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    if not math.isfinite(amount):
        raise ValueError("Amount must be a finite number")
    if amount <= 0:
        raise ValueError("Amount must be positive")


class Account:
    """A single bank account with an owner and a balance."""

    def __init__(self, owner, balance=0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner name is required")
        if isinstance(balance, bool) or not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number")
        if not math.isfinite(balance) or balance < 0:
            raise ValueError("Balance must be a non-negative finite number")
        self.owner = owner.strip()
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        _validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount):
        """Remove money from the account. Balance never goes below zero."""
        _validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
