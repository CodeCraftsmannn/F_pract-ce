#1
class RationalFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        a = abs(self.numerator)
        b = abs(self.denominator)
        while b != 0:
            a, b = b, a % b
        gcd = a
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return RationalFraction(n, d)

    def __iadd__(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduce()
        return self

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return RationalFraction(n, d)

    def __isub__(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduce()
        return self

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return RationalFraction(n, d)

    def __imul__(self, other):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.reduce()
        return self

    def __truediv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return RationalFraction(n, d)

    def __itruediv__(self, other):
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        self.reduce()
        return self

    def to_float(self):
        return self.numerator / self.denominator

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
#-----------------------------------------------------------------------------------

#2
class Matrix2x2:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def add(self, other):
        return Matrix2x2(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def sub(self, other):
        return Matrix2x2(
            self.a - other.a,
            self.b - other.b,
            self.c - other.c,
            self.d - other.d
        )

    def mul(self, other):
        return Matrix2x2(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def mul_num(self, k):
        return Matrix2x2(
            self.a * k,
            self.b * k,
            self.c * k,
            self.d * k
        )

    def div_num(self, k):
        return Matrix2x2(
            self.a / k,
            self.b / k,
            self.c / k,
            self.d / k
        )

    def determinant(self):
        return self.a * self.d - self.b * self.c

    def transpose(self):
        return Matrix2x2(
            self.a,
            self.c,
            self.b,
            self.d
        )

    def __str__(self):
        return f"[{self.a} {self.b}]\n[{self.c} {self.d}]"
#-----------------------------------------------------------------------------------

#3
