# 2675번: 문자열 반복
t = int(input())

for i in range(t):
    result = ''
    r, s = input().split()
    for j in s:
        result += int(r) * j
    print(result)
