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

print(f"Заданы две клетки {kletka1.colvokletok} и {kletka2.colvokletok}")
print(f"Результат сложения: {kletka1 + kletka2}")
print(f"Резульат вычитания: {kletka1 - kletka2}")
print(f"Результат умножения: {kletka1 * kletka2}")
print(f"Результат деления нацело: {kletka1 / kletka2}")

print("\nВывод через функцию:")
print(kletka1.make_order(10))
