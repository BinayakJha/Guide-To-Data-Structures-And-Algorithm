def find_target_index(items, target):
    if len(items) == 0:
        return -1
    start_index = 0
    end_index = len(items) - 1

    while start_index <= end_index:
        mid = int((start_index+end_index)/2)
        if items[mid] == target:
            return mid
        
        is_left_ordered = items[mid] >= items[start_index] # check if left side is ordered or not eg: [3, 4, 5, 6, 7, 8, 0, 1, 2] -> 3 >= 3 -> True  8 >= 3 -> True
        is_right_ordered = items[mid] <= items[end_index] # check if right side is ordered or not eg: [3, 4, 5, 6, 7, 8, 0, 1, 2] -> 3 <= 2 -> False  8 <= 2 -> False

        if is_left_ordered and is_right_ordered: # if both are ordered then we can do binary search
            if target < items[mid]:
                end_index = mid - 1
            else:
                start_index = mid + 1
        elif is_left_ordered: # if left side is ordered then we can do binary search on left side
            if target >= items[start_index] and target < items[mid]: # checks if target is in left side or not
                end_index = mid - 1 
            else:
                start_index = mid + 1 

        elif is_right_ordered: # if right side is ordered then we can do binary search on right side
            if target > items[mid] and target <= items[end_index]: # checks if target is in right side or not
                start_index = mid + 1
            else:
                end_index = mid - 1
        
    return -1




items = [3, 4, 5, 6, 7, 8, 0, 1, 2]
target = 5
print(find_target_index(items, target)) 