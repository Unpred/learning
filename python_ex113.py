def f(x):
    """Возведение в квадрат"""
    return x**2

def fs(name):
    """Возвращает строку"""
    return name

def fx(x, y, z, e=1, t=4):
    """Функция с 2мя необязательными параметрами"""
    return x*y*z*e*t

print(f(3))
print(fs("Hello"))
print(fx(2, 3, 1))

def n(x):
    """Деление на 2"""
    return x // 2

def n1(x):
    """умножение на 4"""
    return x * 4

print(n(4))
print(n1(n(4)))

def str_in_float(x):
    """Преобразование строкового типа в тип с
        плавающей точкой
    """
    try:
        return float(x)
    except(ValueError):
        print("Ошибка ввода")


print(str_in_float("a.05"))
