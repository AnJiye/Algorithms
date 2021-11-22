# 1065번: 한수
n = int(input())
cnt = 0

# 두 자리 수인 경우 무조건 한수
if n < 100:
    cnt = n
# 세 자리 수인 경우 (n은 1000보다 작거나 같은 자연수, 1000은 한수 x)
else:
    cnt = 99    # 1 ~ 99는 무조건 한수
    for i in range(100, n+1):   # 100부터 n까지 반복
        num = list(map(int, str(i)))
        # 연속된 두 수의 차이 비교, 같으면(한수) cnt++
        if num[1] - num[0] == num[2] - num[1]:
            cnt += 1

print(cnt)
