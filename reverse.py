def reverse(list1):
    new_list = []
    while list1:
        num = list1.pop()
        new_list.append(num)
    return new_list

result = reverse([1,2,3,4])
print(result)