import math

def square(a):
    return math.ceil(a*a)

num_a = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(num_a)}")