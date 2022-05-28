#Вычислить число  c заданной точностью d
#	Пример: при d = 0.001,  = 3.141. 10-1d10-10

import math


def Accur(n):
    dt = n.split('.')
    return len(dt[1])

print('Задайте точность для вычисления числа Пи (например 0.001)')
a = input()

n1,n2 = str(math.pi).split('.')
print(f'{n1}.{n2[:Accur(a)]}')