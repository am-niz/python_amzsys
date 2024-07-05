dict1 = {"a": 6, "b": 2, "c": 19}
dict_grater_5 = {key: value for key, value in dict1.items() if value > 5}

print(dict_grater_5)
print(dict_grater_5.items())