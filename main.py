"""
Написать программу решения квадратного уравнения
ax2+bx+c=0

Исходные данные: a,b,c
Результат: корни квадратного уравнения x1 и x2 или сообщение о том, что корней нет.
"""
from math import sqrt

a = 4
b = 10
c = 5

D = b**2 - 4*a*c
if D >=0:
    x1 = (-b + sqrt(D)) / (2 ** a)
    x2 = (-b - sqrt(D)) / (2 ** a)
    print(round(x1,2), round(x2,2))
else:
    print("Корней нет")


