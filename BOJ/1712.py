# 1712번: 손익분기점
# 손익분기점 > A / (C - B)
import math

a, b, c = map(int, input().split())

if (c-b) <= 0:
    point = -1

else:
    point = math.trunc(a/(c-b)) + 1

print(point)
