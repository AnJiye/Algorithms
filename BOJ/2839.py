# 2839번: 설탕 배달
# DP 문제
n = int(input())
d = [0] * 5000

for i in range(5, n+1):
    d[i] = min(d[i-3] + 1, d[i-5] + 1)

print(d[n])
