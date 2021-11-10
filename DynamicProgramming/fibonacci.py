# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
# 동일한 함수가 반복 호출되기 때문에 x가 커질수록 심각한 문제 발생 가능
"""
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
"""

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현 (탑다운 다이나믹 프로그래밍)
"""
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))
"""

# 피보나치 수열: 보텀업 다이나믹 프로그래밍 소스코드
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
