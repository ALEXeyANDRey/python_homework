#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

print('Введите числа через пробел')
a = input()
dt = a.split()
dt = list(map(int, dt))

unique = [item for item in dt if dt.count(item) == 1]
print(unique)