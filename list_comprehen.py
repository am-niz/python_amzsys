sqr_lst = [x*x for x in range(10)]
print(sqr_lst)

evn_lst = [x for x in range(10) if x % 2 == 0]
print(evn_lst)

lst = ["apple", "banana", "orange", "pinaple"]

upper_case_list = [item.upper() for item in lst]
print(upper_case_list)

list1 = ["ant", "bird", "me", "elephant"]

three_char_list = [item for item in list1 if len(item) > 3]
print(three_char_list)

divisible_by_3_5 = [number for number in range(1,101) if number % 3 == 0 and number % 5 == 0]
print(divisible_by_3_5)

list3 = [[1,2,3],[4,5,6],[7,8,9]]
flatter_list = [item for sub_list in list3 for item in sub_list]
print(flatter_list)

list4 = ["apple", "banana", "cherry"]
new_list = [i[0] for i in list4]
print(new_list)

pythagorous_triples = [(a,b,c) for a in range(1,20) for b in range(a,20) for c in range(b,20) if a**2 + b**2 == c**2]
print(pythagorous_triples)

vowels = ["a","e","i","o","u"]
str = "nizam"
with_out_vowels = [i for i in str if i not in vowels]
print(with_out_vowels)

dic = {"nizam": 98, "anees": 97, "punya": 83}
dic_to_list = [(k,v) for k, v in dic.items()]
print(dic_to_list)

str = "nizamma"
unique = set(str)
print(unique)


a = 10
b = 30

a, b = b, a
print(a,b)

if len(str) == len(set(str)):
    print(True)
else:
    print(False)