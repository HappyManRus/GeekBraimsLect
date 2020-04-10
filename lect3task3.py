def my_calc(arg1, arg2, arg3):
    try:
        a = [arg1, arg2, arg3]
        a.sort(reverse=True)
        return (float(a[0]) + float(a[1]))
    except:
        return "Ошибка, среди чисел были не числа, а чтото большее)"


arg1 = 8
arg2 = 5
arg3 = 6

print(f"Сумма двух наибольших чисел равна: {my_calc(arg1, arg2, arg3)}")
