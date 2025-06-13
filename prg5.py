# 10. Count the number of lines, words, and characters in a text file

# Replace 'sample.txt' with your filename
filename = 'sample.txt'

# Initialize counters
line_count = 0
word_count = 0
char_count = 0

# Open the file
with open(filename, 'r') as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

# Display results
print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
