class car:
    what_class = "Родителский класс"

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(
            f"Вы создали класс {self.what_class}, c именем машины {name}, цвет {color}, скорость {speed}, и типом отношения к полиции {self.is_police} ")

    def go(self):
        print(f"У вас машина класса {self.what_class}. Внимание, машина начала движение!")

    def stop(self):
        print(f"У вас машина класса {self.what_class}. Машина остановилась. Ручник подняли?")

    def turn(self, direction):
        print(f"У вас машина класса {self.what_class}. Машина повернула на {direction}!")

    def show_speed(self):
        print(f"У вас машина класса {self.what_class}. Ваша скорость {self.speed}")


class TownCar(car):
    what_class = "TownCar"

    def show_speed(self):
        if self.speed > 60:
            {
                print(
                    f"У вас машина класса {self.what_class}. Вы превышаете скорость, максимум для вас 60, а вы несетесь {self.speed}. You are bad boy!")
            }
        else:
            print(f"У вас машина класса {self.what_class}. Ваша скорость {self.speed}")


class SportCar(car):
    what_class = "SportCar"


class WorkCar(car):
    what_class = "WorkCar"

    def show_speed(self):
        if self.speed > 40: {
            print(f"Вы превышаете скорость, максимум для вас 40, а вы несетесь {self.speed}")
        }


class PoliceCar(car):
    what_class = "PoliceCar"


towncarclass = TownCar(70, "желтый", "Toyota", False)
towncarclass.show_speed()
towncarclass.speed = 50;
towncarclass.show_speed()

workcarclass = WorkCar(45, "Красный", "BMW", False)
workcarclass.show_speed()
workcarclass.go()
workcarclass.turn("лево")

policecarclass = PoliceCar(15, "Голубой", "Lada", True)
print(policecarclass.color)
policecarclass.color = "Розовый"
print(policecarclass.color)

sportcarclass = SportCar(280, "Красный", "Ferrary", False)
print(sportcarclass.speed)
