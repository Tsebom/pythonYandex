s = input()

result = ''

if len(s) % 2 == 0 and s[:int(len(s)/2)] == s[int(len(s)/2):][::-1]:
    result = "YES"
else:
    result = "NO"

print(result)
