# Coding Efficiency Examples

This repository contains small but meaningful examples focused on writing cleaner and more efficient code. Today’s example highlights how to improve Python output formatting using a single `print("\n")` instead of multiple `print()` statements.

---

## 📌 Example: Efficient Multiplication Table

**File:** `multiplication_table.py`

This script prints a multiplication table from a start value to a stop value using nested loops. It includes a minor but thoughtful improvement: instead of using two `print()` statements to insert a blank line between rows, it uses `print("\n")` to achieve the same result more cleanly.

```python
def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(x * y, end=' ')
        print('\n')  # cleaner than using two print() statements
