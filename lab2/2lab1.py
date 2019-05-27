import random
my_number = int(random.uniform(1,4))#генерация случайного числаа от 1 до 4
print('Требуется ввести число от 1 до 4: ')
user_number = int(input())
while (user_number == my_number):
    print('Загаданное число равно вашему, повторите ввод числа')
    user_number = int(input())
else:
    print('Загаданное число не равно вашему')