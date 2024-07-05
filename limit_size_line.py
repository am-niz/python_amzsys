import sys

def wrap_lines(file, size):
    with open("file3.txt", "r") as f:
        contents = f.readlines()
        for line in contents:
            while len(line) > size:
                print(line[:size+1])
                line = line[size:]
            if line:
                print(line)


file, size = sys.argv[1], int(sys.argv[2])
wrap_lines(file, size)
