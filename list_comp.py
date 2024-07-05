# a = range(4)
# print(list(a))
# b = range(0,10,3)
# print(list(b))
# lst = [x for x in a if x % 2 == 0]
# print(lst)
#
# print(list(zip(a,b)))
#
# list1 = [x*y for x, y in zip(a,b)]
# print(list1)

# list1 = [(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0]
# print(list1)

def square(x):return x%2==0

print(list(filter(square, range(10))))