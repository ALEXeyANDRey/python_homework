#Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

list=[1, 5, 2, 3, 4, 6, 1, 7]
list1=[1]

for i in range(len(list)):
    if list[i]==list1[-1]+1:
        list1.append(list[i])
    if len(list1)==3: break
    

print(list1)