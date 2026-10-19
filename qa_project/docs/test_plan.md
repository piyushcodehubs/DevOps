# Test Plan: Mini Bank

| | |
|---|---|
| Project | Mini Bank (Python) |
| Tester | _your name_ |
| Date | _date_ |
| Environment | Linux, Python 3.x, pytest, pytest-cov, flake8 |

## 1. Scope

**In scope:** `Account` (deposit, withdraw, validation), `Bank` (add, find,
transfer, totals), storage (save/load JSON), command line interface.

**Out of scope:** graphical interface, networking, real money handling,
security and authentication.

## 2. Test types

| Type | What is tested | Where | Tool |
|---|---|---|---|
| Unit | One class or function on its own | `tests/test_account.py`, `tests/test_bank.py` | pytest |
| Integration | Account + Bank + file storage together | `tests/test_integration.py` | pytest, `tmp_path` |
| System | Whole app through the CLI, start to finish | `tests/test_system_cli.py` and manual runs | pytest, `python -m app.cli` |
| Edge cases / errors | Empty, wrong type, negative, NaN, huge values, corrupted files | `tests/test_edge_cases.py` | pytest `parametrize` |
| User acceptance | A real person completes realistic tasks | `docs/uat_notes.md` | manual |
| Performance | Lookup speed with 5000 accounts | `scripts/benchmark.py` | timeit, cProfile |
| Static / style | Style and common mistakes | whole project | flake8 |

## 3. Entry criteria

- Code is written and runs without syntax errors.
- Virtual environment is set up and `pip install -r requirements.txt` worked.

## 4. Exit criteria (when testing is finished)

- All automated tests pass.
- Line coverage of `app/` is 80% or more (record the real number below).
- Every bug found is logged and either fixed or listed as a known issue.
- UAT done with at least one real tester.
- Peer code review done and feedback handled.

## 5. Risks

- Floating-point amounts (0.1 + 0.2) can give tiny rounding differences. For
  real money, store whole cents or use `decimal.Decimal`.
- The CLI is tested with scripted input, so real terminal behaviour (paste,
  Ctrl+C) must be checked by hand.

## 6. Results summary (fill in at the end)

| Measure | Result |
|---|---|
| Total automated tests | |
| Passed / failed | |
| Coverage | |
| Bugs found / fixed / open | |
| flake8 warnings | |
