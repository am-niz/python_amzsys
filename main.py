marks = [98, 99, 100]
name = ["nizam", "punya", "aneese"]

# new_list = zip(name, marks)
#
# print(list(new_list))

# for name, marks in zip(name, marks):
#     print(name, marks)


print(sum(marks))

result = " ".join(name)
print(result)

def product(list1):
    prod = 1
    for num in list1:
        prod = prod * num
    return prod

num = 6
factorial = product(list(range(1, num+1)))
print(factorial)