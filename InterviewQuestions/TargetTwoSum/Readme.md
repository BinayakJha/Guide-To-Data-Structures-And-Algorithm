# Target Two Sum

Given an ```array``` of unsorted unique integers, write a program that returns an array of arrays of the index of the two numbers that add up to a ```target``` number.

## Important Points To Note:

* The array is unsorted and unique.
* The array can contain negative numbers.
* The array can contain positive numbers.
* The same pair of indexes should only be included once
* The order of the returned array and its items does not matter

```python
# Input
array = [4, -3, 80, 2, 9, 13, 5, 8]
target = 7

# Output: get_target_indexes(array, target)
[[1, 5], [3, 7]]
```