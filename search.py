import sys

def search(file, strng):
    try:
        with open("file3.txt", "r") as f:
            for line in f:
                if strng in line:
                    print(line, end="")
    except FileNotFoundError:
        print(f"Error: File '{file}' not found")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    file, strng = sys.argv[1], sys.argv[2]
    search(file, strng)
