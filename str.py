arr = []

while True:
    n = input()
    if n == '':
        break
    elif n.startswith('#'):
        continue
    elif n.count('#'):
        arr.append(n.split('#')[0])
    else:
        arr.append(n)

for i in range(len(arr)):
    print(arr[i])
