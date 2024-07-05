dict = {"banana": 3, "apple": 2, "cherry": 4}

dict_sort = {key: dict[key] for key in sorted(dict)}
print(dict_sort)
dict_interchange = {dict[key]: key for key in dict}
print(dict_interchange)