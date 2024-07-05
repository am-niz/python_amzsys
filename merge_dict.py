dict1 = {"a": 1, "b":2, "c":3}
dict2 = {"d":5, "a":2, "e": 10}

merged_dict = {k: dict1.get(k,0) + dict2.get(k,0) for k in set(dict1) | set(dict2)}
print(merged_dict)

list1 = range(0,100)
print(list(list1[0::2]))

list1 = ["hi", "hellow"]
r = sum([list1])
print(r)