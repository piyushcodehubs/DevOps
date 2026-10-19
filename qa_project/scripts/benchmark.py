"""Performance check: linear search (before) vs dictionary lookup (after).

Run from the project root:   python scripts/benchmark.py
Profile it yourself with:    python -m cProfile -s cumtime scripts/benchmark.py | head -20
"""
import sys
import timeit
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.account import Account  # noqa: E402
from app.bank import Bank  # noqa: E402

ACCOUNTS = 5000
LOOKUPS = 200


def main():
    bank = Bank()
    for i in range(ACCOUNTS):
        bank.add_account(Account(f"user{i}", 100))
    target = f"user{ACCOUNTS - 1}"  # worst case for a linear search

    slow = timeit.timeit(lambda: bank.find_slow(target), number=LOOKUPS)
    fast = timeit.timeit(lambda: bank.find(target), number=LOOKUPS)

    print(f"{ACCOUNTS} accounts, {LOOKUPS} lookups of the last account")
    print(f"Before (find_slow, linear): {slow:.4f} s")
    print(f"After  (find, dict):        {fast:.6f} s")
    print(f"Speed-up: about {slow / fast:,.0f}x faster")


if __name__ == "__main__":
    main()
