#По двум заданным числам проверить является ли одно квадратом втором
a = int (input('Введите первое целое число '))
b = int (input('Введите второе целое число '))

def IsSquare(x,y):
    if y ==x**2 or x ==y**2: return True
    else: return False

if IsSquare (a,b): print('Одно из чисел яляется квадратом второго')
else: print ('Введенные числа не соответсвуют условию задачи')