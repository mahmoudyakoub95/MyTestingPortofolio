

## Original Code

```python
def is_shipping_free(price, numberOfItems, isPrimeShoppingMember):
    print("Additional Statement 1")
    if price > 50 or isPrimeShoppingMember:
        print("Additional Statement 2")
    if price > 25 and numberOfItems < 3:
        print("Additional Statement 3")
    elif price > 10 and numberOfItems == 1:
        print("Additional Statement 4(discount)")
        return False
    return True
    print("Additional Statement 5")
```

## 1. Statement Coverage

For statement coverage, we count all executable statements, including `if` and `elif`. We exclude only the function definition.

There are **10 statements** in total:

- 5 print statements
- 2 return statements
- 3 decision statements (`if` and `elif`)

The last print statement (`Additional Statement 5`) is unreachable because it comes after `return True`.

The tests cover the other 9 statements.

Statement coverage = (9 / 10) × 100 = **90%**

### Without the unreachable statement

After removing the unreachable statement, 9 statements remain, and all 9 are covered.

Statement coverage = (9 / 9) × 100 = **100%**

## 2. Branch Coverage

Based on the four branches marked in the flowchart:

- **Branch 1:** The execution path through the first decision's No outcome and the `elif` condition's True outcome.
- **Branch 2:** The execution path through the first decision's Yes outcome and the second `if` condition's True outcome.
- **Branch 3:** The execution path where the second `if` condition and the `elif` condition are both False, leading to `return True`.
- **Branch 4:** The path to `Additional Statement 5`, which is unreachable because it comes after `return True`.

The tests cover the first three branches. Branch 4 cannot be executed.

Total branches = 4

Covered branches = 3

Branch coverage = (3 / 4) × 100 = **75%**

### Without the unreachable branch

After excluding the unreachable branch, 3 branches remain, and all 3 are covered.

Branch coverage = (3 / 3) × 100 = **100%**

## Final Results

| Coverage type | Original code | Without unreachable statement/branch |
|---|---:|---:|
| Statement coverage | 90% | 100% |
| Branch coverage | 75% | 100% |
