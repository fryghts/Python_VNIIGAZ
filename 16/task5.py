my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
s = sorted(my_dict.keys(), key = lambda x: my_dict[x], reverse = True)[:3]
