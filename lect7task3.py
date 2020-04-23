class Kletka:
    def __init__(self, colvokletok):
        self.colvokletok = colvokletok

    def __add__(self, other):
        return self.colvokletok + other.colvokletok

    def __sub__(self, other):
        a = self.colvokletok - other.colvokletok
        if a > 0:
            return self.colvokletok - other.colvokletok
        else:
            return "Результат отрицательный. Такое недопустимо. Проверьте кол-во клеток"

    def __mul__(self, other):
        return self.colvokletok * other.colvokletok

    def __truediv__(self, other):
        return (self.colvokletok // other.colvokletok)

    def make_order(self, colvoraid):
        a = ""
        for i in range(1, self.colvokletok + 1):
            a += "*"
            if (i % colvoraid == 0):
                a += "\n"
        return a


kletka1 = Kletka(51)
kletka2 = Kletka(23)

print(kletka1 + kletka2)
print(kletka1 - kletka2)
print(kletka1 * kletka2)
print(kletka1 / kletka2)

print(kletka1.make_order(10))
