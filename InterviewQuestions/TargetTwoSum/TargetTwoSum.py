def get_target_indexes(array, target):
  # Your solution here
    output = []
    for i in range(len(array)):
        for j in range(1, len(array)):
            if i != j and i < j and array[i]+array[j] == target:
                output.append([i,j])
    return output


array = [1, 2]
target = 3

print(get_target_indexes(array, target))

