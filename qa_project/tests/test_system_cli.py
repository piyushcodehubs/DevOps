"""System tests: drive the whole application through its command line loop.

The input and print functions are replaced, so a whole user session can be
scripted as a list of typed lines and the screen output can be checked.
"""
from app import cli


def scripted(lines):
    feed = iter(lines)

    def _input(prompt=""):
        try:
            return next(feed)
        except StopIteration:
            raise EOFError from None

    return _input


def run_session(lines):
    screen = []
    bank = cli.run(input_fn=scripted(lines), print_fn=screen.append)
    return bank, "\n".join(screen)


def test_full_user_journey():
    bank, screen = run_session([
        "create", "Ravi",
        "deposit", "Ravi", "100",
        "withdraw", "Ravi", "30",
        "balance", "Ravi",
        "quit",
    ])
    assert "Created account for Ravi" in screen
    assert "Ravi's balance: 70.00" in screen
    assert bank.find("Ravi").balance == 70
    assert screen.endswith("Goodbye")


def test_overdraft_shows_error_and_keeps_running():
    bank, screen = run_session([
        "create", "Ravi",
        "withdraw", "Ravi", "50",
        "deposit", "Ravi", "10",
        "quit",
    ])
    assert "Error: Insufficient funds" in screen
    assert bank.find("Ravi").balance == 10


def test_non_numeric_amount_shows_error():
    _, screen = run_session(["create", "Ravi", "deposit", "Ravi", "abc", "quit"])
    assert "Error: Amount must be a number" in screen


def test_negative_amount_shows_error():
    _, screen = run_session(["create", "Ravi", "deposit", "Ravi", "-5", "quit"])
    assert "Error: Amount must be positive" in screen


def test_unknown_account_shows_error():
    _, screen = run_session(["balance", "Nobody", "quit"])
    assert "Error: No account for 'Nobody'" in screen


def test_duplicate_account_shows_error():
    bank, screen = run_session(["create", "Ravi", "create", "ravi", "quit"])
    assert "already exists" in screen
    assert len(bank) == 1


def test_empty_owner_shows_error():
    _, screen = run_session(["create", "", "quit"])
    assert "Error: Owner name is required" in screen


def test_unknown_command_shows_help():
    _, screen = run_session(["dance", "quit"])
    assert "Unknown command" in screen


def test_input_ending_without_quit_exits_cleanly():
    _, screen = run_session(["create", "Ravi"])
    assert screen.endswith("Goodbye")
