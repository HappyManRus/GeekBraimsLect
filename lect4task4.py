import random

new_list = [random.randint(0, 10) for i in range(20)]
new_list2 = [i for i in new_list if new_list.count(i) == 1]
print(f"Начальный список: {new_list}")
print(f"Измененый список: {new_list2}")
