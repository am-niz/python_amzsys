class RationNumbers:
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationNumbers):
            other = RationNumbers(other)
        n = self.n * self.d + self.d * other.n
        d = self.d * other.d
        return RationNumbers(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationNumbers):
            other = RationNumbers(other)
        n = self.n * self.d - self.d * other.n
        d = self.d * other.d
        return RationNumbers(n,d)

    def __str__(self):
        return f"{self.n}/{self.d}"


a = RationNumbers(1, 2)
b = RationNumbers(1, 2)
c = a - b
print(c)