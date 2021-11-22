# 2609번: 최대공약수와 최소공배수

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


a, b = map(int, input().split())
g = gcd(a, b)
lcm = int(a * b / g)

print(g)
print(lcm)
