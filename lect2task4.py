string_user = input("Введите строку из нескольких слов, через пробел: ")
list_user = string_user.split()
for list_elemnt in list_user:
    print(list_elemnt[:10])

# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
