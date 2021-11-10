# 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0

while k:
    a.sort()
    b.sort()
    if a[0] < b[len(b)-1]:
        a[0], b[len(b)-1] = b[len(b)-1], a[0]
    else:
        break
    k -= 1

for i in range(n):
    sum += a[i]

print(sum)
