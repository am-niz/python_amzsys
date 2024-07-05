def find_non_duplicates(list1):
    count_dic = {}
    for item in list1:
        if item in count_dic:
            count_dic[item] = count_dic[item] + 1
        else:
            count_dic[item] = 1

    non_duplicates = [item for item in list1 if count_dic[item] == 1]
    print(non_duplicates)

find_non_duplicates([1, 2, 3, 4, 4, 2, 1])

