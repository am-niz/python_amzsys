def group(list1, size):
    return [list1[i:i+size] for i in range(0, len(list1), size)]

result = group([1, 2, 3, 4, 5, 6, 7],3)
print(result)