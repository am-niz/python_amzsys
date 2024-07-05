def unique(list1, key=None):
    new_list = []
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    print(new_list)

list1 = [1, 1, 2, 2, 3]
unique(list1)

unique_list = [i for i in set(list1)]
print(unique_list)