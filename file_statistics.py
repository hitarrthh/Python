import os
file_path = 'exp9.txt' 
file_size = os.path.getsize(file_path)
print(f"File Size (in bytes): {file_size}")
num_lines = 0
num_words = 0
num_chars = 0
with open(file_path, 'r') as file:
    for line in file:
        words = line.split()  
        num_lines += 1
        num_words += len(words)
        num_chars += sum(len(word) for word in words)
print(f"Number of Lines: {num_lines}")
print(f"Number of Words: {num_words}")
print(f"Number of Characters: {num_chars}")
