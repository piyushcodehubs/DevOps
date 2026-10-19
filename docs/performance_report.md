# Performance Report

## 1. Measure first

Run the benchmark on your own machine, a few times, and use your own numbers.

```bash
python scripts/benchmark.py
python -m cProfile -s cumtime scripts/benchmark.py | head -20
```

`cProfile` shows which functions take the most time. Optimize the one at the
top of the list, not the one you guess is slow.

## 2. The bottleneck

`Bank.find_slow()` checks every account one by one, so the time grows with the
number of accounts (linear, O(n)). With 5000 accounts and the target at the
end of the list, every lookup walks the whole list.

## 3. The improvement

`Bank.find()` keeps a dictionary from owner name to account, so a lookup takes
about the same time however many accounts exist (O(1) on average). The price
is a little extra memory and keeping the dictionary in step when accounts are
added.

## 4. Results (replace with your own numbers)

| Function | Before | After | Change |
|----------|--------|-------|--------|
| `find_slow` vs `find`, 5000 accounts, 200 lookups | _your number_ s | _your number_ s | _x times faster_ |

_Example from one run on a cloud sandbox (yours will differ): 0.1031 s before,
0.000040 s after, roughly 2,500 times faster._

## 5. Checks that the optimization is safe

- `test_find_slow_and_find_agree` confirms both return the same account.
- All other tests still pass after the change.

## 6. Other ideas to try

- Try 100, 1000 and 50000 accounts and note how the gap changes.
- Time `load_account` and `save_account` on many files.
- Use `python -m timeit` for quick one-line timings.
