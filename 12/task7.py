db = {}
while s:=input():
    name, item, vol = s.split()
    vol = int(vol)
    db.setdefault(name, {}).setdefault(item, 0)
    db[name][item] += vol

print(db)
    
