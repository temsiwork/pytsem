# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#
# 2 2
# 4


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
def summa(a, b):
    if b == 0:
        return 0
    return summa(a, b - 1) + a

print(summa(a, b))