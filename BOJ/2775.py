# 2775번: 부녀회장이 될테야
# import sys
# sys.setrecursionlimit(10000)

t = int(input())
count = [[0] * 14 for _ in range(14)]
dfsdf = 1


def solve(a, b):
    if a == 0:
        # count[a][b] = b
        return b
    if b == 1:
        return 1
    if count[a][b] == 0:
        count[a][b] = solve(a, b-1) + solve(a-1, b)
        return solve(a, b-1) + solve(a-1, b)


for i in range(t):
    k = int(input())
    n = int(input())
    print(solve(k, n))
