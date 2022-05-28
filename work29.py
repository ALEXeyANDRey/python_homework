#Найти НОК двух чисел

import math
list1=[]
with open(r'file29.txt', 'r') as data:
    for item in data:
        list1.append(item)
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    print(math.lcm(list1[0], list1[1]))