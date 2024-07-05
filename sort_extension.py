def ext_sort(lst):
    sorted_list = sorted(lst, key=lambda x: len(x))
    print(sorted_list)

lst = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
ext_sort(lst)

res = sorted(lst, key=lambda x: len(x.split(".")[-1]))
print(res)