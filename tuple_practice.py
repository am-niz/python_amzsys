t = (1, 2, 3, [1, 2, 3])
t[3].append(4)
print(t)

def sum_product(a, b):
    return (a+b, a*b)

print(sum_product(4, 5))

t1 = (1, 2, 2, 3, 4)
t2 = (5, 6, 7, 8)
t3 = t1 + t2
print(t3)

t3 = t1.count(2)
print(t3)

ind = t2.index(5)
print(ind)

t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(t[1][1])

def swap_first_lasst(t):
    return t[-1:] + t[1:-1] + t[:1]

r = swap_first_lasst((1, 2, 3, 4, 5))
print(r)

t = (1,2,3,4,5)
t1 = t[0:2]
t2 = t[2:]
print(t1, t2)



