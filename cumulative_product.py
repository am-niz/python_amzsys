def cumulative_pod(list1):
    prod = 1
    cumulative_poduct_list = []
    for i in list1:
        prod = prod * i
        cumulative_poduct_list.append(prod)
    print(cumulative_poduct_list)

cumulative_pod([1, 2, 3, 4, 5])