class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. Проект {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем ручку. Проект {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем карандаш. Проект {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Рисуем маркер. Проект {self.title}")


classpen = Pen("Супер ручка")
classpen.draw()

class_Pencil = Pencil("Карандаш будущего")
class_Pencil.draw()
print(class_Pencil.title)

class_Handle = Handle("Маркер невидимка")
class_Handle.draw()

class_stat = Stationery("Старое прошлое)")
class_stat.draw()
