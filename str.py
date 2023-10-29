N = int(input())
r = 'зайка'
result = 0

for i in range(N):
    result += input().count(r)

print(result)
