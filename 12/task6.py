words_num = int(input())
eng_to_rus = {}
for _ in range(words_num):
    s = input()
    eng, rus = s.split('-')
    rus = rus.split(',')
    eng = eng.strip()
    rus = list(map(str.strip, rus))
    eng_to_rus[eng] = rus

rus_to_eng = {}
for eng, rus_list in eng_to_rus.items():
    for rus in rus_list:
        rus_to_eng.setdefault(rus, []).append(eng)
    
