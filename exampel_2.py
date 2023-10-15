import math

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2

S = math.sqrt(p * (p - a) * (p - b) * (p - c))

alpha = math.degrees(math.asin((2 * S) / (a * b)))
beta = math.degrees(math.asin((2 * S) / (a * c)))
gama = math.degrees(math.asin((2 * S) / (c * b)))
print(alpha, beta, gama)

if alpha == 90 or beta == 90 or gama == 90:
    print('100%')
elif alpha > 90 or beta > 90 or gama > 90:
    print('велика')
elif alpha < 90 and beta < 90 and gama < 90:
    print('крайне мала')


'''
def min_num(x, y):
    if x < y:
        return x
    else:
        return y


def max_num(x, y):
    if x > y:
        return x
    else:
        return y


def min_num(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


def mid_num(a, b, c):
    if (b < a < c) or (c < a < b):
        return a
    elif (a < b < c) or (c < b < a):
        return b
    else:
        return c


def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def print_step(string):
    for i in range((8 - len(string)) // 2):
        print(' ', end='')

    print(string, end='')

    for i in range((8 - len(string)) // 2):
        print(' ', end='')
'''
