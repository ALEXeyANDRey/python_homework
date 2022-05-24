#Найти произведение пар чисел в списке.
#  #Парой считаем первый и последний элемент, второй и предпоследний и т.д. #
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

def M_Pairs(list):
    k = len(list)-1
    res = []
    if len(list)%2 == 0:
        for i in range((len(list)//2)):
            res.append(list[i]*list[k-i])
    else:
        for i in range((len(list)//2)+1):
            res.append(list[i]*list[k-i])
    return res

ls = [2,3,4,5,6]

print(f'Произведение пар числе в списке {ls} равно {M_Pairs(ls)}')
