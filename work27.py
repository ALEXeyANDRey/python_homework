#Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел

def Min_Max(str):
    new_str = str.split(' ')
    min = int(new_str[0])
    max = int(new_str[0])

    for i in range(len(new_str)):
        new_str[i] = int(new_str[i])
        if (new_str[i] < min):
            min = new_str[i]
        if (new_str[i] > max):
            max = new_str[i]

    print(f'Минимум = ', min,'Максимум = ', max)


my_str = input('Введите несколько цифр через пробел ')
Min_Max(my_str)