# 10250번: ACM 호텔
import math

t = int(input())
room = ''

for i in range(t):
    h, w, n = map(int, input().split())
    if h >= n:
        room = str(n)+'01'
    else:
        floor = n % h
        order = math.ceil(n / h)
        if floor == 0:
            floor = h
        if order < 10:
            order = '0' + str(order)
        room = str(floor)+str(order)
    print(room)
