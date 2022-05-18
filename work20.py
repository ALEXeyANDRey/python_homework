#Определить, присутствует ли в заданном списке строк, некоторое число 

def Find(sp, el):
    flag = False
    for item in sp:
        if (item == el):
            flag = True
            break

    if flag:
        print('Заданное число присутствует ')
    else:
        print('Заданного числа в списке нет ')


my_spisok = [134, 34, 786, 567, 406, 89, 901]
a = 40


Find(my_spisok, a)