# 5618번: 공약수
# 시간 초과
import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


for i in range(1, n):
    result = gcd(data[i-1], data[i])

# 시간 초과
for i in range(1, result+1):
    if result % i == 0:
        print(i)
