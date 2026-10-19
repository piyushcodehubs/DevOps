"""A bank that holds many accounts."""


class AccountNotFoundError(Exception):
    """Raised when no account exists for the given owner."""


class Bank:
    def __init__(self):
        self._accounts = []
        self._by_owner = {}

    def __len__(self):
        return len(self._accounts)

    @staticmethod
    def _key(owner):
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string")
        return owner.strip().lower()

    def add_account(self, account):
        """Register an account. Owner names are unique (case-insensitive)."""
        key = self._key(account.owner)
        if key in self._by_owner:
            raise ValueError(f"Account for '{account.owner}' already exists")
        self._accounts.append(account)
        self._by_owner[key] = account

    def find_slow(self, owner):
        """Linear search through every account. Kept for the benchmark."""
        key = self._key(owner)
        for account in self._accounts:
            if self._key(account.owner) == key:
                return account
        raise AccountNotFoundError(f"No account for '{owner}'")

    def find(self, owner):
        """Dictionary lookup. Fast even with many accounts."""
        try:
            return self._by_owner[self._key(owner)]
        except KeyError:
            raise AccountNotFoundError(f"No account for '{owner}'") from None

    def transfer(self, from_owner, to_owner, amount):
        """Move money between two accounts.

        Everything is validated before any balance changes, so a failed
        transfer leaves both accounts untouched.
        """
        source = self.find(from_owner)
        target = self.find(to_owner)
        if source is target:
            raise ValueError("Cannot transfer to the same account")
        source.withdraw(amount)  # raises before changing anything if invalid
        target.deposit(amount)

    def total_deposits(self):
        """Sum of all balances held by the bank."""
        return sum(account.balance for account in self._accounts)
