with open('file.txt', encoding = 'utf-8') as file:
    max_word = ''
    for line in file:
        word = max(line.split(), key=len)
        if len(word) > len(max_word):
            max_word = word
            
print(max_word)
