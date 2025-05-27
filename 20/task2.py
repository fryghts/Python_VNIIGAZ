#bn = b0*(q**n)
#b1 = b0*q
#bk = b0*q**k
# b0*q**k < bmax
# q**k > bmax/b0

# 1 > bmax/b0/q**k
class grange:
    def __init__(self, b0, q, bmax):
        self.b0 = b0
        self.q = q
        self.bmax = bmax
    def __len__(self):
        bi = abs(self.bmax/self.b0)
        i=0
        if not(-1 <= self.q <= 1):
            while bi > 1:
                bi /= self.q
                i += 1
        else:
            return 0
        return i
    def __bool__(self):
        return bool(len(self))
    def __getitem__(self, idx):
        if type(idx) == slice:
            if abs(self[idx.start]) < abs(self.b0):
                start = self.b0
            else:
                start = self[idx.start]
            if abs(self[idx.start]) > abs(self.bmax):
                stop = self.bmax
            else:
                stop = self[idx.stop]
                
            if idx.step == None:
                return grange(start, self.q, stop)
            else:
                return grange(start, idx.step, stop)
        if type(idx) == int and idx >= 0 :
            bi = self.b0*(self.q**idx)
            if abs(bi) <= abs(self.bmax):
                return bi
            else:
                raise StopIteration
        else:
            raise TypeError('Некорректный индекс')
    def __str__(self):
        return f'grange({self.b0},{self.q},{self.bmax})'
    def __repr__(self):
        return f'grange({self.b0},{self.q},{self.bmax})'
    
