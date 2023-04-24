# Recursive Binary Search
def recursive_binary_search(array, target, lower_bound, upper_bound):
    # Base case 1: element not found
    if lower_bound > upper_bound:
        return -1
    
    midpoint_index = (lower_bound + upper_bound) // 2
    midpoint_item = array[midpoint_index]

    # Base case 2: target found
    if midpoint_item == target:
        return midpoint_index

    # Recursive case: tighten your bounds based on target location
    if midpoint_item < target:
        return recursive_binary_search(array, target, midpoint_index + 1, upper_bound)

    if midpoint_item > target:
        return recursive_binary_search(array, target, lower_bound, midpoint_index - 1)

    return -1

# Test cases
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
lower_bound = 0
upper_bound = len(array) - 1
print(recursive_binary_search(array, target, lower_bound, upper_bound))