import math


class Angled:
    def __init__(self, length=None, wigth=None, diagonal=None):
        self.lenght = length
        self.wight = wigth
        self.diagonal = diagonal
        if length == None or wigth == None:
            self.get_other
        if diagonal == None:
            self.get_diagonal

    @property
    def get_other(self):
        match self.lenght:
            case None:
                self.lenght = int(
                    math.sqrt(self.diagonal ** 2 - self.wight**2))
        self.wight = int(math.sqrt(self.diagonal ** 2 - self.lenght**2))

    @property
    def get_diagonal(self):
        self.diagonal = int(math.sqrt(self.lenght ** 2 + self.wight**2))

    @property
    def perimeter(self):
        return (self.lenght + self.wight) * 2

    @property
    def radius(self):
        return self.diagonal / 2

    @property
    def diameter(self):
        return self.diagonal

    @property
    def area(self):
        return self.lenght * self.wight


first = Angled(None, 4, 5)
print(first.lenght)
print(first.area)