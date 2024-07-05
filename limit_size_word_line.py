import sys


def word_wrap(filename, width):
    try:
        with open(filename, 'r') as f:
            for line in f:
                # print(line)
                line = line.rstrip('\n')
                print(line)# Remove trailing newline
                words = line.split()  # Split line into words
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) <= width:
                        current_line += word + " "
                    else:
                        print(current_line.rstrip())
                        current_line = word + " "
                if current_line:
                    print(current_line.rstrip())

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wordwrap.py <filename> <width>")
    else:
        filename = sys.argv[1]
        try:
            width = int(sys.argv[2])
            word_wrap(filename, width)
        except ValueError:
            print("Error: Width must be an integer.")
