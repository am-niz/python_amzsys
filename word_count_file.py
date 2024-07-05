import pydoc
def word_count():
    with open("file3.txt", "r") as f:
        words = f.read().split(" ")

        # frequency of the words that occured in the file
        words_count_dict = {word: words.count(word) for word in set(words)}

        #printing the items according to the descending order of the values
        sorted_dict = sorted(words_count_dict.items(), key= lambda item: item[1], reverse=True)
        str1 = " ".join(str(item) for tuples in sorted_dict for item in tuples)
        str1_words = str1.strip()
        # print(str1_words)
        for i in str1_words:
            print(i, end=" ")
        # for i in range(0, len(str1_words), 2):
        #     print(str1_words[i] ,str1_words[i+1])

word_count()
pydoc math