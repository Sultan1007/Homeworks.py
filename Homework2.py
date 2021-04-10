# Complex
# 1) magic method (+, -, /, *)
# 2) return Complex ->
# complex2 = Complex(2, 5)
# complex3 = complex1 + complex2
# 3) __str__

class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - self.real, self.imag - other.imag)

    def __truediv__(self, other):
        return Complex(self.real / other.real, self.imag / other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.imag + self.imag * other.imag
        new_complex = Complex(real, imag)
        return new_complex

    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f'{self.real}{self.imag}i'



complex1 = Complex(1, 2)
complex2 = Complex(2, 5)
result = complex1 * complex2
complex3 = complex1 + complex2
complex4 = complex1 + complex2
complex5 = complex1 - complex2
complex6 = complex1 / complex2
print(complex3.real)
print(complex3.imag)
print()
print(complex4.real)
print(complex4.imag)
print()
print(complex5.real)
print(complex5.imag)
print()
print(complex6.real)
print(complex6.imag)
