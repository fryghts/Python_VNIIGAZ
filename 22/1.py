class strExt(str):
    def __add__(self,other):
        if isinstance(other, str):
            if self.isdigit() and other.isdigit():
                return strExt(int(self)+int(other))
            else:
                return super().__add__(other) 
        else:
            return self + type(self)(other)
    def __sub__(self,other):
        if isinstance(other, str):
            if self.isdigit() and other.isdigit():
                return strExt(int(self)-int(other))
            else:
                return super().__sub__(other) 
        else:
            return self - type(self)(other)
    def __radd__(self,other):
        return self.__add__(other)
    def __rsub__(self,other):
            return self.__sub__(other)
