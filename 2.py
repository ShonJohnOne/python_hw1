"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

x = int(input("Введите Х: "))
y = int(input("Введите Y: "))
z = int(input("Введите Z: "))


def Predicate(x,y,z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result

print(Predicate(x,y,z))