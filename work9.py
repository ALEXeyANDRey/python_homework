# Указав номер четверти прямоугольной системы координат ,
#  показать допустимые значения координат для точек этой четверти

tochka = int(input('Ввести номер четверти координат: '))

if (tochka == 1):
    print('x > 0 and y > 0')
if (tochka == 2):
    print('x < 0 and y > 0')
if (tochka == 3):
    print('x < 0 and y < 0')
if (tochka == 4):
    print('x > 0 and y < 0')
