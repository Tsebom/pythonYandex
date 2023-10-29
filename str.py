s = input()

result = 'NO'

for i in range(int(len(s) / 2)):
    if s[i] == s[len(s) - 1 - i]:
        result = 'YES'
    else:
        result = 'NO'
        break

print(result)
