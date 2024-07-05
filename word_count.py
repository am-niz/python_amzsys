import sys
def word_count(file1):
    count = {}
    with open(file1, "r") as f:
        for lines in f:
            lines = lines.strip()
            words = lines.split(" ")
            for word in words:
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1

    print(count)
    print(count.items())
    del count["you"]
    print(count)

file = sys.argv[1]
word_count(file)
