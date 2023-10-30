N = input()

arr = []

for i in range(int(N)):
    n = input().find('зайка')

    if n != -1:
        arr.append(n + 1)
    else:
        arr.append('Заек нет =(')

for i in range(len(arr)):
    print(arr[i])
