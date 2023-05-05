import math

def circle(r):
    res = math.pi * math.pow(r, 2)
    print("Площадь круга:", res)
def prm(a, b):
    res = a * b
    print("Площадь прямоугольника:", res)
def treg(a, h):
    res = 1/2 * a * h
    print("Площадь треугольника:", res)

print("1 - Круг;\n2 - Прямоугольник;\n3 - Треугольник.")
try:
    figure = int(input("Введите номер фигуры для вычисления ее площади:"))
except ValueError:
    print("Ошибка ввода !")

if figure == 1:
    r = int(input("Введите радиус r:"))
    circle(r)
elif figure == 2:
    a = int(input("Введите сторону a:"))
    b = int(input("Введите сторону b:"))
    prm(a, b)
elif figure == 3:
    a = int(input("Введите основание a:"))
    h = int(input("Введите основание a:"))
    treg(a, h)
else:
    print("Такого пункта нет!")