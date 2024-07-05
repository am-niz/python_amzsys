def char_count(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return len(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

def word_count(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

# Example usage:
filename = "foo.txt"
print(f"Character count in '{filename}': {char_count(filename)}")
print(f"Word count in '{filename}': {word_count(filename)}")
