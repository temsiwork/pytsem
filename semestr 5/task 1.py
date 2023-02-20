# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def degree(a, b):
    if b == 0:
        return 1
    return degree(a, b - 1) * a

f = int(input())
k = int(input())
print(degree(f, k))