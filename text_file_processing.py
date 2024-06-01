file_input = 'exp9.txt'
with open(file_input, 'r') as file:
    for line in file:
        word = line.strip().split()
        new_ans = '#'.join(word)
        print(new_ans)