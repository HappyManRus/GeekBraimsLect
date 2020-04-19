import time


class TrafficLight:
    # атрибуты класса
    __collor = ["\033[31mКрасный", "\033[33mЖелтый", "\033[32mЗеленый", "\033[33mЖелтый"]
    times = [7, 2, 7, 2]

    # методы класса
    def running(self):
        stop_triger = 0
        while True:
            for i in range(len(self.__collor)):
                print(f"\r{self.__collor[i]}", end=' ')
                time.sleep(self.times[i])  # in seconds
            stop_triger += 1
            if stop_triger == 500:
                break


myclass = TrafficLight()
myclass.running()
