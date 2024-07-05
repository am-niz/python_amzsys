def reverse_line():
    with open("file2.txt","r") as f:
        lines_in_list = f.readlines()
        print(lines_in_list)
        new_order = lines_in_list[::-1]
        print(new_order)
        print("".join(new_order))

reverse_line()

# content2 = "\n".join(lines)