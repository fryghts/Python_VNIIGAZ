def capitalize(word):
    c = word[0]
    if 'a' <= c <= 'z' or 'а' <= c <= 'я':
        return chr(ord(c)-32)+word[1:]
    if c == 'ё':
        return 'Ё'+word[1:]
    return word

