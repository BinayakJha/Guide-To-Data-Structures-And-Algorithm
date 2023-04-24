def search_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1 # last column
    # while loop checks if the row and column are within the matrix
    while row  < len(matrix) and col >= 0:
        # checks the value at the current row and column
        if matrix[row][col] == target:
            return [row, col] # return the row and column
        # if not then check if the value is greater than the target
        elif matrix[row][col] > target:
            col -= 1 # if it is then move to the left
        else:
            row += 1 # if it is not then move down

    return [-1, -1]
        

matrix = [
  [0, 2, 5, 8, 10],
  [1, 4, 9, 15, 20],
  [3, 7, 14, 19, 21],
  [17, 22, 23, 24, 25]
]
target = 19

print(search_matrix(matrix, target))