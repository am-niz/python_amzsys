list1 = [1, 2, 3, 3, 2, 1, 0, 9, 8]

duplicate_elements_list = set([i for i in list1 if list1.count(i) > 1])
print(duplicate_elements_list)