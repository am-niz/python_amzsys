def line_rev():
    with open("file2.txt","r") as f:
        contents = f.readlines()
        # print(contents)
        rev_str = "".join(contents)
        # print(rev_str)
        print(rev_str[::-1])
line_rev()
