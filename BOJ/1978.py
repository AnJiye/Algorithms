# 1978번: 소수 찾기
n = int(input())
data = list(map(int, input().split()))
count = 0


def solve(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


for i in data:
    if i > 1 and solve(i):
        count += 1

print(count)
