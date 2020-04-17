import random

new_list = [str(random.randint(0, 100)) for i in range(20)]
try:
    fwrite = open("text_5.txt", 'w', encoding='utf-8')
    fwrite.write(' '.join(new_list))
    fwrite.close()

    fread = open("text_5.txt", encoding='utf-8')
    sumfile = 0
    for line in fread:
        listline = line.split()
        sumfile = sum(int(i) for i in listline)
    print(sumfile)
    fread.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
except:
    print("Некоректные данные!")
