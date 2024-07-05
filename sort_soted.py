a = [1,8,3,3,2]
a.sort()
print(a)

b = [[7,2], [3,4], [5,3]]


def function(x):
    return x[0]


b.sort(key=function)
print(b)