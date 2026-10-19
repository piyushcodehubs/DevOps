"""Save and load accounts as JSON files."""
import json

from app.account import Account


def save_account(account, path):
    """Write an account to a JSON file."""
    data = {"owner": account.owner, "balance": account.balance}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def load_account(path):
    """Read an account from a JSON file.

    Raises FileNotFoundError if the file is missing, and ValueError if the
    file is not valid JSON or does not contain valid account data.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    try:
        owner = data["owner"]
        balance = data["balance"]
    except (KeyError, TypeError) as exc:
        raise ValueError(f"Missing field in account file: {exc}") from None
    return Account(owner, balance)
