class Vector:
    def __add__(self, other):
        if type(other) is not Vector:
            other = float(other)
        elif type(other) is Vector and self.size != other.size:
            raise ValueError
            return
        new = Vector(self.size)
        if type(other) is Vector:
            for i in range(self.size):
                new.values[i] = self.values[i] + other.values[i]
        else:
            for i in range(self.size):
                new.values[i] = self.values[i] + other
        return new

    def __sub__(self, other):
        if type(other) is not Vector:
            other = float(other)
        elif type(other) is Vector and self.size != other.size:
            raise ValueError
        return self.__add__(other * -1)

    def __mul__(self, other):
        if type(other) is not Vector:
            other = float(other)
        elif type(other) is Vector and self.size != other.size:
            raise ValueError
            return
        if type(other) is Vector:
            return sum(self.values[i]
                       + other.values[i] for i in range(self.size))
        else:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] * other
            return new

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError
        other = float(other)
        return self.__mul__(1 / other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if type(other) is not Vector:
            new = Vector([float(other)] * self.size)
            return new.__mul__(self)
        return other.__sub__(self)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f'values: {self.values} size: {self.size}'

    def __repr__(self):
        return f'Vector({self.values})'

    def __init__(self, values):
        if type(values) is list:
            if not self.valid_list(values):
                values = []
            new = []
            for i in values:
                try:
                    new.append(float(i))
                except ValueError:
                    new = []
                    break
            self.values = new
            self.size = len(values)
        if type(values) is int:
            self.values = self.float_range(values)
            self.size = values
        if type(values) is range:
            self.values = self.float_range(values)
            self.size = len(values)

    def float_range(self, values):
        lst = []
        if type(values) is int:
            for i in range(values):
                lst.append(float(i))
        if type(values) is range:
            for i in values:
                lst.append(float(i))
        return lst

    def valid_list(self, lst):
        for i in lst:
            try:
                float(i)
            except ValueError:
                return False
        return True
