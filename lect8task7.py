class complesclass:
    def __init__(self, complexnum):
        self.complexnum = complexnum

    def __add__(self, other):
        dei_part = self.complexnum.real + other.complexnum.real
        mnin_part = self.complexnum.imag + other.complexnum.imag
        return complex(dei_part, mnin_part)

    def __mul__(self, other):
        dei_part = self.complexnum.real * other.complexnum.real - self.complexnum.imag * other.complexnum.imag
        mnin_part = self.complexnum.real * other.complexnum.imag + self.complexnum.imag * other.complexnum.real
        return complex(dei_part, mnin_part)

    def __str__(self):
        return str(self.complexnum)


comnum1 = complesclass(complex(4, 7))
comnum2 = complesclass(complex(3, 2))

print(f"Представлены комплексные числа {comnum1} и {comnum2}")
print(f"Результат умножения: {comnum1 * comnum2}")
print(f"Результат сложения: {comnum1 + comnum2}")
