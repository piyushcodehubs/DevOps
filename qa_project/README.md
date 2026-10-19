# Mini Bank: Testing and QA Project (Python)

A small bank application (accounts, deposits, withdrawals, transfers, JSON
storage, command line interface) built to practise the Testing and Quality
Assurance phase: unit, integration, system and edge-case testing, debugging,
performance, code review and documentation.

## Setup (Linux)

```bash
sudo apt install -y python3 python3-pip python3-venv   # Ubuntu/Debian/Mint
cd qa_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the tests

Run everything from the project root (the `qa_project` folder).

```bash
python -m pytest                                   # all tests
python -m pytest tests/test_account.py             # one file
python -m pytest -k "transfer"                     # tests with "transfer" in the name
python -m pytest --pdb                             # open the debugger on a failure
python -m pytest --cov=app --cov-report=term-missing --cov-report=html
xdg-open htmlcov/index.html                        # coverage report in the browser
flake8 app tests scripts                           # style check
```

## Run the application and the benchmark

```bash
python -m app.cli              # try the app by hand (system testing)
python scripts/benchmark.py    # performance before/after
```

## What is where

| Folder / file | Purpose | Task item |
|---|---|---|
| `app/account.py` | Account class with validation | code under test |
| `app/bank.py` | Many accounts, transfers, lookup | code under test |
| `app/storage.py` | Save/load accounts as JSON | code under test |
| `app/cli.py` | Command line interface | code under test |
| `tests/test_account.py` | Unit tests | unit testing |
| `tests/test_bank.py` | Bank with Account | unit / integration |
| `tests/test_integration.py` | Account + Bank + files | integration testing |
| `tests/test_edge_cases.py` | Bad and extreme input | edge cases, error handling |
| `tests/test_system_cli.py` | Scripted user sessions | system testing |
| `scripts/benchmark.py` | Slow vs fast lookup | performance optimization |
| `docs/test_plan.md` | What, how and when you test | documentation |
| `docs/test_cases.md` | Test case table | documentation |
| `docs/bug_log.md` | Bugs found and fixed | debugging, documentation |
| `docs/uat_notes.md` | User acceptance testing notes | UAT |
| `docs/performance_report.md` | Before and after numbers | performance |
| `docs/code_review.md` | Peer review checklist and feedback | code review |

## Try breaking the code (a good way to get real bug-log entries)

A test suite is only useful if it fails when the code is wrong. Make one small
change, run `python -m pytest`, see which test catches it, then undo it and log
what you learned in `docs/bug_log.md`.

- In `app/account.py`, change `amount <= 0` to `amount < 0`. The test for
  depositing or withdrawing `0` should fail.
- In `Account.withdraw`, change `amount > self.balance` to
  `amount >= self.balance`. The "withdraw exact balance" test should fail.
- In `Bank.transfer`, swap the `withdraw` and `deposit` lines and trigger an
  overdraft. Think about what state the accounts are left in.

## Adapting this to your own project

The structure stays the same for any Python project: put your code in `app/`,
write unit tests for each function, integration tests for modules that work
together, edge-case tests for bad input, one system test for the full user
flow, then fill in the `docs/` files with your own results.

## Submission checklist

- [ ] All tests pass (`python -m pytest`)
- [ ] Coverage report generated (80% or more) and screenshot saved
- [ ] `docs/test_cases.md` Actual and Result columns filled in
- [ ] System test steps run by hand with `python -m app.cli`
- [ ] `docs/uat_notes.md` completed with a real tester
- [ ] `docs/bug_log.md` has at least a few real entries
- [ ] `docs/performance_report.md` has your own before/after numbers
- [ ] `docs/code_review.md` completed with a peer
- [ ] Known issues listed
