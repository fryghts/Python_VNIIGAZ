class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return type(self)(self.val+other.val)
    def __repr__(self):
        return f'A({self.val})'
class B(A):
    def __init__(self, val):
        super().__init__(val)
        print('Привет, Мир!')
    def __mul__(self,other):
        from numbers import Integral
        if isinstance(other, Integral):
            return type(self)(self.val*other)
        return type(self)(self.val*other.val)
    def __rmul__(self,other):
        return self.__mul__(other)
    def __add__(self, other):
        from numbers import Number
        if isinstance(self, A) and isinstance(other, A):
            return super().__add__(other)
        elif isinstance(other, Number):
            return type(self)(self.val+other)
        raise Exception
    def __radd__(self,other):
        return self.__add__(other)
    def __repr__(self):
        return f'B({self.val})'

