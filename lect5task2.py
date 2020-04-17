try:
    f = open("text_2.txt")
    num = 1
    for line in f:
        listline = line.split()
        print(f"в строке номер {num} содержится {len(listline)} слов")
        num += 1
    f.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
