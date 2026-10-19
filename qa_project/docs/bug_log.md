# Bug Log

Record every bug you find while testing, including ones you fix straight away.
Break the code on purpose (see the README) if your tests find nothing, and log
what you learn.

| ID | Description | Found by | Root cause | Fix | Status |
|----|-------------|----------|------------|-----|--------|
| B1 | _EXAMPLE, replace with your own:_ `withdraw("abc")` gave a confusing error instead of a clear one | edge case test | no type check in `withdraw` | added `_validate_amount()` used by deposit and withdraw | Fixed |
| B2 | | | | | |
| B3 | | | | | |

**Status values:** Open, Fixed, Won't fix, Known issue.

## How to debug a failing test

1. Read the failure message: which line, expected value, actual value.
2. Reproduce it with one command: `python -m pytest tests/test_x.py::test_name`.
3. Drop into the debugger: `python -m pytest --pdb`. Useful commands: `n` next
   line, `s` step into, `p variable` print, `l` list code, `c` continue, `q` quit.
4. Fix the cause, not the symptom. Re-run all tests to check nothing else broke.
5. Add or keep a test that would have caught the bug, then log it above.

## Known issues (not fixed)

- Amounts are stored as floats, so very long chains of decimal amounts can
  drift by tiny fractions. A real banking system would use `decimal.Decimal`
  or integer cents.
- Accounts are only saved one at a time (`save_account`); there is no
  save-the-whole-bank feature.
