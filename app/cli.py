"""Command line interface. Run with:  python -m app.cli"""
from app.account import Account
from app.bank import AccountNotFoundError, Bank

HELP = "Commands: create, deposit, withdraw, balance, quit"


def _parse_amount(text):
    try:
        return float(text)
    except ValueError:
        raise ValueError("Amount must be a number") from None


def run(bank=None, input_fn=input, print_fn=print):
    """Main loop. input_fn and print_fn can be replaced in tests."""
    bank = bank if bank is not None else Bank()
    print_fn(HELP)
    while True:
        try:
            command = input_fn("> ").strip().lower()
        except EOFError:
            break
        if command == "quit":
            break
        try:
            if command == "create":
                account = Account(input_fn("Owner: "))
                bank.add_account(account)
                print_fn(f"Created account for {account.owner}")
            elif command == "deposit":
                account = bank.find(input_fn("Owner: "))
                account.deposit(_parse_amount(input_fn("Amount: ")))
                print_fn(f"New balance: {account.balance:.2f}")
            elif command == "withdraw":
                account = bank.find(input_fn("Owner: "))
                account.withdraw(_parse_amount(input_fn("Amount: ")))
                print_fn(f"New balance: {account.balance:.2f}")
            elif command == "balance":
                account = bank.find(input_fn("Owner: "))
                print_fn(f"{account.owner}'s balance: {account.balance:.2f}")
            else:
                print_fn(f"Unknown command. {HELP}")
        except (ValueError, TypeError, AccountNotFoundError) as exc:
            print_fn(f"Error: {exc}")
    print_fn("Goodbye")
    return bank


if __name__ == "__main__":
    run()
