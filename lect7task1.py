class MyClass:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        newmc = []

        for i in range(len(self.param)):
            el = []
            for j in range(len(self.param[i])):
                el.append(self.param[i][j] + other.param[i][j])
            newmc.append(el)

        return MyClass(newmc)

    def __str__(self):
        s = ""
        for i in self.param:
            for j in i:
                s += (str(j)).center(7)
                # s += ("{:7d}".format(j))
            s += "\n"
        return s


mc = MyClass([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
mc2 = MyClass([[5, 8, 1], [6, 7, 3], [4, 5, 9]])
print(mc)
print(mc2)
print(mc + mc2)
