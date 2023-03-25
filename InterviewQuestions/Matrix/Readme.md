# Walk a Matrix
Question From: **Skilled.dev**
You are given a ```matrix``` represented by an ```r x c``` two-dimensional array of integers. Starting at the root ```matrix[row = 0][column = 0]``` and walking from the perimeter of the matrix towards the center, you want to touch each element once in the matrix by traversing it clockwise in spiral order. Return a 1-dimensional array of all the elements from the matrix in the order you visited them.

**Write a function ```walk_matrix``` that takes an ```r x c``` 2D array and returns a 1D array of all the elements in the matrix printed in clockwise order.**

```python
# Input
matrix = [
  [0, 1, 2, 3],
  [11, 12, 13, 4],
  [10, 15, 14, 5],
  [9, 8, 7, 6]
]

# Output: walkMatrix(matrix)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

