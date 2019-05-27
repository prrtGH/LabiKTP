from random import choice
from string import digits
lst='0'#задание строки для проверки
while ('3' not in lst):#пока нет 3 в строке
#генерация строки путем выбора из чисел длиной 6 символов
    lst = ''.join(choice(digits) for i in range(6))
print('Случайная строка из чисел из 6 символов хотя бы с одной 3: ',lst)