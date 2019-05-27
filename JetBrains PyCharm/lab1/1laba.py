print("Решение уравнения")
a=float(input("Введите а= "))
b=float(input("Введите b= "))
c=float(input("Введите c= "))
while (c-a)==0:
    print("Деление на ноль, на ноль делить нельзя!(c-a=0)")
    a=float(input("Введите а= "))
    c=float(input("Введите c= "))
else:
    d=abs(1-a*pow(b,c)-a*(b*b-c*c)+(b-c+a)*(12+b)/(c-a))
    print("Ответ: ", d)
