def sort_by_age(age_list):
    for i in range(len(age_list)):
        for j in range(0,len(age_list)-i-1):
            if age_list[j] > age_list[j+1]:
                temp = age_list[j]
                age_list[j] = age_list[j+1]
                age_list[j+1] = temp
    return age_list

age_list = [33, 25, 99, 33, 50, 42]
print(sort_by_age(age_list))