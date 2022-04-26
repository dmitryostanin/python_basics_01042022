base_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(base_list)
result_list = [num for num in base_list if base_list.count(num) == 1]
print(result_list)
