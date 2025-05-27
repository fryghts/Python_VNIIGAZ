from itertools import chain

a = {'a':10, 'b':2, 'd': 500}
b = {'a':0, 'c':100, 'd':-1}

#d = {f'{key}_{1 if val == a.get(key) else 2}' if key in a and key in b else key : val for key, val in chain(a.items(), b.items())}
d = {}
for key, val in chain(a.items(), b.items()):
    if key in a and key in b:
        d[f'{key}_{1 if val == a.get(key) else 2}'] = val
    else:
        d[key] = val
