from itertools import count, cycle

""" вывожу микс их count и cycle, плюс вставляю элементы cycle в разные позиции
    Например:
    А10
    1А0
    10А
"""

c_co = 0
for elco in count(7):
    с_el = 0
    for elcy in cycle("ABC"):
        if с_el > 6:
            break
        else:
            for k in range(len(str(elco)) + 1):
                print(str(elco)[0:k] + elcy + str(elco)[k:])
        с_el += 1
    if c_co > 6:
        break
    c_co += 1
