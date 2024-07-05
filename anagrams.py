def find_angrams(list1):
    anagrams_dict = {}

    for word in list1:
        sorted_word = sorted(word)
        sorted_word = "".join(sorted_word)

        if sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = [word]
        else:
            anagrams_dict[sorted_word].append(word)

    result = list(anagrams_dict.values())
    for item in result:
        print(item)

find_angrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
