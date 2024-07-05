str = "abracadrabra"

count_chr_dict = {char: str.count(char) for char in set(str)}
print(count_chr_dict)
