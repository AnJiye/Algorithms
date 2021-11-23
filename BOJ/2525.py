# 2525번: 오븐 시계

a, b = map(int, input().split())
c = int(input())
min = b + c

if min < 60:
    m = min
    h = a
else:
    m = min % 60
    h = a + min // 60

if h > 23:
    h -= 24

print(h, m)
