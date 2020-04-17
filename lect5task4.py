my_dict = dict(One="Один", Two="Два", Three="Три", Four="Четыре", Five="Пять", Six="Шесть", Seven="Семь",
               Eight="Восемь", Nine="Девять", Ten="Десять")
try:
    f = open("text_4.txt", encoding='utf-8')
    fwrite = open("textRUS_4.txt", 'w', encoding='utf-8')
    for line in f:
        listline = line.split()
        fwrite.write(my_dict.get(listline[0]) + " " + listline[1] + " " + listline[2] + "\n")
    f.close()
    fwrite.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
except:
    print("Некоректные данные!")
