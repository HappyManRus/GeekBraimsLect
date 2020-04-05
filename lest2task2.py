strange_list = []
while True:
    temp_prt= input("Введите элемент(пусто для завершения) : ")
    if temp_prt == "":
        break
    strange_list.append(temp_prt)
print(f"Вы ввели список: {strange_list}")
number = 0
while number < len(strange_list)//2*2:
    strange_list[number], strange_list[number+1] = strange_list[number+1], strange_list[number]
    number += 2

print(f"Измененный список: {strange_list}")

#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#Вариант 2
#number = 0
#while number < len(strange_list)//2*2:
#    strange_list.insert(number + 2, strange_list[number])
#    strange_list.pop(number)
#    number += 2