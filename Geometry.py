import math


class Angled:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    @property
    def diagonal(self):
        return int(math.sqrt(self.lenght ** 2 + self.width ** 2))

    @property
    def perimeter(self):
        return (self.lenght + self.width) * 2

    @property
    def radius(self):
        return self.diagonal / 2

    @property
    def diameter(self):
        return self.diagonal

    @property
    def area(self):
        return self.lenght * self.width

    @classmethod
    def automagic(cls, width=None, length=None, area=None, perimeter=None, diagonal=None, radius=None, diameter=None):
        if width is not None and length is not None:
            return cls(length=length, width=width)

        # In case only one side is provided
        side = width if width is not None else length
        if side is not None:
            if diagonal is not None or diameter is not None:
                dia_ = diagonal or diameter
                length = math.sqrt(dia_ ** 2 - side ** 2)
                return cls(length=length, width=side)
            elif area is not None:
                length = area / side
                return cls(length=length, width=side)
            elif perimeter is not None:
                length = perimeter / 2 - side
                return cls(length=length, width=side)
            elif radius is not None:
                length = math.sqrt((radius * 2) ** 2 - side ** 2)
                return cls(length=length, width=side)

        # TODO: In cases when no side is provided
        if area is not None:
            if perimeter is not None:
                side = (perimeter / 2 + math.sqrt((perimeter / 2) ** 2 - 4 * area)) / 2
                return cls(length=side,width=area / side)
            if diagonal is not None or diameter is not None:
                dia_ = diagonal or diameter
                side = (math.sqrt(dia_**2 + 2* area) - math.sqrt(dia_**2 - 2*area)) / 2
                width = area/side
                return cls(length=side,width=width)
            if radius is not None:
                dia_ = radius * 2
                side = (math.sqrt(dia_**2 + 2* area) - math.sqrt(dia_**2 - 2*area)) / 2
                width = area/side
                return cls(length=side,width=width) 
        
        if perimeter is not None:
            if diagonal is not None or diameter is not None:
                dia_ = diagonal or diameter
                D = (perimeter ** 2) * 4 - (perimeter ** 2 - (dia_**2) * 4) * 8
                side = ((perimeter * 2) + math.sqrt(D)) / 8
                width = perimeter / 2 - side
                return cls(length=side,width=width)
            if radius is not None:
                dia_ = radius * 2
                D = (perimeter ** 2) * 4 - (perimeter ** 2 - (dia_**2) * 4) * 8
                side = ((perimeter * 2) + math.sqrt(D)) / 8
                width = perimeter / 2 - side
                return cls(length=side,width=width)
                

if __name__ == "__main__":
    first = Angled.automagic(radius=2.5,perimeter=14)
    print(first.area)
    print(first.diagonal)
    print(first.diameter)
    print(first.radius)
    print(first.perimeter)
    print(first.width)
    print(first.lenght)
