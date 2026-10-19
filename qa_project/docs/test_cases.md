# Test Cases

Run `python -m pytest -v`, then fill in the **Actual** and **Result** columns
from what you really saw. The last column names the pytest test that automates
the case, so you can find it quickly.

| ID | Type | Description | Input | Expected | Actual | Result | pytest test |
|----|------|-------------|-------|----------|--------|--------|-------------|
| TC01 | Unit | New account starts at zero | `Account("Ravi")` | balance 0 | | | `test_new_account_defaults_to_zero_balance` |
| TC02 | Unit | Deposit increases balance | balance 100, deposit 50 | balance 150 | | | `test_deposit_increases_balance` |
| TC03 | Unit | Withdraw decreases balance | balance 100, withdraw 40 | balance 60 | | | `test_withdraw_decreases_balance` |
| TC04 | Unit | Withdraw exact balance | balance 100, withdraw 100 | balance 0 | | | `test_withdraw_exact_balance_leaves_zero` |
| TC05 | Unit | Withdraw more than balance | balance 100, withdraw 500 | ValueError "Insufficient funds", balance stays 100 | | | `test_withdraw_more_than_balance_raises_and_keeps_balance` |
| TC06 | Unit | Find ignores case and spaces | `"  ravi "` | returns Ravi's account | | | `test_find_ignores_case_and_spaces` |
| TC07 | Unit | Duplicate owner rejected | add `"RAVI"` when Ravi exists | ValueError "already exists" | | | `test_duplicate_owner_is_rejected` |
| TC08 | Unit | Transfer moves money | Ravi (100) to Anita (50), 30 | Ravi 70, Anita 80 | | | `test_transfer_moves_money` |
| TC09 | Unit | Failed transfer changes nothing | Anita to Ravi, 500 | ValueError, balances stay 100 / 50 | | | `test_failed_transfer_changes_nothing` |
| TC10 | Unit | Transfer to same account | Ravi to `"ravi"` | ValueError "same account" | | | `test_transfer_to_same_account_is_rejected` |
| TC11 | Integration | Save then load an account | Ravi, balance 125 | same owner and balance | | | `test_save_and_load_roundtrip` |
| TC12 | Integration | Transfer, save, reload | transfer 30, save both, load both | 70 / 80, total 150 | | | `test_transfer_then_persist_then_reload` |
| TC13 | Integration | Load a file that does not exist | missing path | FileNotFoundError | | | `test_loading_missing_file_raises` |
| TC14 | Integration | Load a corrupted file | `this is not json` | ValueError | | | `test_loading_corrupted_file_raises_value_error` |
| TC15 | Integration | Load file with a missing field | `{"owner": "Ravi"}` | ValueError "Missing field" | | | `test_loading_file_with_missing_field_raises` |
| TC16 | Edge | Empty or blank owner | `""`, `"   "`, `None`, `123` | ValueError | | | `test_invalid_owner_is_rejected` |
| TC17 | Edge | Zero or negative amount | `0`, `-1`, `-0.01` | ValueError "positive", balance unchanged | | | `test_non_positive_amounts_are_rejected` |
| TC18 | Edge | Wrong type amount | `"abc"`, `"50"`, `None`, `[10]`, `True` | TypeError, balance unchanged | | | `test_wrong_type_amounts_are_rejected` |
| TC19 | Edge | NaN and infinity | `nan`, `inf`, `-inf` | ValueError "finite" | | | `test_nan_and_infinity_are_rejected` |
| TC20 | Edge | Very large amount | `10**12` | accepted, balance `10**12` | | | `test_huge_amount_is_handled` |
| TC21 | Edge | Floating point sum | deposit 0.1 then 0.2 | balance about 0.3 | | | `test_floating_point_amounts_need_approx` |
| TC22 | System | Full user journey in the CLI | create Ravi, deposit 100, withdraw 30, balance | "Ravi's balance: 70.00" | | | `test_full_user_journey` |
| TC23 | System | Overdraft in the CLI | withdraw more than balance | "Error: Insufficient funds", app keeps running | | | `test_overdraft_shows_error_and_keeps_running` |
| TC24 | System | Non-numeric amount in the CLI | amount `abc` | "Error: Amount must be a number" | | | `test_non_numeric_amount_shows_error` |
| TC25 | System | Unknown account in the CLI | balance of `Nobody` | "Error: No account for 'Nobody'" | | | `test_unknown_account_shows_error` |

## Manual system test (run `python -m app.cli` yourself)

Do these by hand and write what you saw.

| ID | Steps | Expected | Actual | Result |
|----|-------|----------|--------|--------|
| MS01 | `create`, owner `Ravi` | "Created account for Ravi" | | |
| MS02 | `deposit`, `Ravi`, `500` | "New balance: 500.00" | | |
| MS03 | `withdraw`, `Ravi`, `9999` | "Error: Insufficient funds" | | |
| MS04 | `deposit`, `Ravi`, `-5` | "Error: Amount must be positive" | | |
| MS05 | `balance`, `Ravi` | "Ravi's balance: 500.00" | | |
| MS06 | type `hello` at the prompt | "Unknown command" and the help line | | |
| MS07 | press Ctrl+D at the prompt | app prints "Goodbye" and exits | | |
| MS08 | `quit` | "Goodbye" and exits | | |
