import itertools


def fibo_gen():
    factorials = 1
    for el in itertools.count():
        factorials *= (el + 1)
        if el > 100:
            break
        yield factorials


count = 0
for el in fibo_gen():
    print(el)
    count += 1
    if count >= 15:
        break
