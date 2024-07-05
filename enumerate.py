def enumerate1(lst):
    new_lst = []
    for index, value in enumerate(lst):
        new_lst.append((index, value))
    print(new_lst)

enumerate1(["nizam", "amjad", "aneese"])