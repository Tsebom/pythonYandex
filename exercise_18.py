n = int(input())
k = 1
i = 1

a = []


def b(x):
    sr = ''
    for i in range(x):
        sr += ' '
    return sr


while k <= n:
    s = ''
    for j in range(i):
        s += str(k) + ' '
        k += 1
        if k > n:
            break
    a.append(s)
    i += 1

space = len(a)

for i in a:
    space -= 1
    print(f'{b(space)}{i}')

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


'''
