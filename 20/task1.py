from random import shuffle, choice
class door:
    def __init__(self, prize=False):
        self.prize = prize
        self.open = False

class show:
    def __init__(self):
        self.doors = [door(), door(), door(prize=True)]
        shuffle(self.doors)
    def start(self):
        self.player = choice(self.doors)
    def open_other_door(self):
        new_door = choice(list(filter(lambda x:not x.prize and x is not self.player, self.doors)))
        new_door.open = True
    def change_door(self):
        self.player = list(filter(lambda x: not x.open and x is not self.player, self.doors))[0]
    def reveal(self):
        return self.player.prize

changed_counter = 0

for i in range(10000):
    s = show()
    s.start()
    s.open_other_door()
    s.change_door()
    changed_counter += s.reveal()
    
not_changed_counter = 0

for i in range(10000):
    s = show()
    s.start()
    s.open_other_door()
    not_changed_counter += s.reveal()

print(f'Игрок поменял мнение: {changed_counter/100}%')
print(f'Игрок не поменял мнение: {not_changed_counter/100}%')
