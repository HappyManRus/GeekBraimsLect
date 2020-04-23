from abc import ABC, abstractmethod

class clotnes(ABC):
    def __init__(self, nameclot):
        self.nameclot = nameclot

    @abstractmethod
    def rashod(self):
        return self.nameclot

class palto(clotnes):
    def __init__(self, size):
        super().__init__("Пальто")
        self.size = size

    @property
    def rashod(self):
        return "Расход ткани " + str(round((self.size/6.5 + 0.5),1))

class suit(clotnes):
    def __init__(self, height):
        super().__init__("Костюм")
        self.height = height

    @property
    def rashod(self):
        return "Расход ткани " + str(round((2*self.height + 0.3),1))

palto1 = palto(3)
print (palto1.nameclot)
print(f"Размер пальто {palto1.size}")
print(palto1.rashod)

suit1 = suit(5)
print (suit1.nameclot)
print(f"Ростовка костюма {suit1.height}")
print(suit1.rashod)
