# Code Review

| | |
|---|---|
| Author | _your name_ |
| Reviewer | _peer's name_ |
| Date | |
| Files reviewed | `app/account.py`, `app/bank.py`, `app/storage.py`, `app/cli.py`, `tests/` |

## Review checklist

Mark each item Yes / No / N/A and add a note where the answer is No.

**Readability**
- [ ] Names of variables, functions and classes say what they are or do
- [ ] Functions are short and do one job
- [ ] Docstrings or comments explain the "why", not the obvious
- [ ] Consistent style (run `flake8 app tests scripts`)

**Correctness**
- [ ] Inputs are validated (type, empty, negative, huge, NaN)
- [ ] Errors use the right exception type with a clear message
- [ ] A failed operation leaves data unchanged (for example a failed transfer)
- [ ] Files are opened with `with` and an explicit encoding

**Maintainability**
- [ ] No copy-pasted code that should be a shared function
- [ ] No magic numbers or hard-coded paths
- [ ] Modules have one clear responsibility
- [ ] Easy to add a new feature without rewriting old code

**Tests**
- [ ] Every public function has at least one test
- [ ] Tests cover normal, edge and error cases
- [ ] Test names describe the behaviour being checked
- [ ] Tests do not depend on each other or on leftover files

## Feedback received

| # | File / line | Comment from reviewer | Severity | Action taken | Done |
|---|-------------|-----------------------|----------|--------------|------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## What I learned

- 

## Review I gave (peer's code)

| # | File / line | My comment | Suggestion |
|---|-------------|------------|------------|
| 1 | | | |
| 2 | | | |
