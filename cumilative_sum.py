import math


def cumulative_sum(list1):
    sum = 0
    new_list = []
    for i in list1:
        sum = sum + i
        new_list.append(sum)
    print(new_list)

list1 = [1, 2, 3, 4]
cumulative_sum(list1)

cumilative_list_sum = [sum(list1[:i+1]) for i in range(len(list1))]
print(cumilative_list_sum)