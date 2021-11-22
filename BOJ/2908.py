# 2908번: 상수
a, b = input().split()
reverse_a, reverse_b = int(a[::-1]), int(b[::-1])

print(reverse_a) if reverse_a > reverse_b else print(reverse_b)
