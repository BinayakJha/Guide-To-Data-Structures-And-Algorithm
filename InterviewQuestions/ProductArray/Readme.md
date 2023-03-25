# Product Array
Question From: **Skilled.dev**

Given an array of integers, write a function <i>build_product_array </i> that returns an array where each item is the product of all the items in the input array except for the item at that index.


Constraints:

1) Solve this without using division
2) You can create a **results** array, and it won't count against your space complexity
3) Memory may be a concern though, so try to limit your use of additional data structures

```python
# Input
input = [1, 2, 3, 4, 5]

# Output: build_product_array(input)
# [2*3*4*5, 1*3*4*5, 1*2*4*5, 1*2*3*5, 1*2*3*4]
[120, 60, 40, 30, 24]
```



