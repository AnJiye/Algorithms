# 17479번: 정식당
# 시간 초과
import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
general = dict()
special = dict()
service = []
order = []
# general_price = 0
# special_price = 0
price = 0
count = 0


def check(order, kinds):
    # print(''.join(map(str, order)))
    if ''.join(map(str, order)) in kinds:
        print(kinds)


# 일반 메뉴
for i in range(a):
    key, value = sys.stdin.readline().rstrip().split()
    general[key] = int(value)

# 스페셜 메뉴
for i in range(b):
    key, value = sys.stdin.readline().rstrip().split()
    special[key] = int(value)

# 서비스 메뉴
for i in range(c):
    service.append(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

# 주문
for i in range(n):
    # menu = sys.stdin.readline().rstrip()
    order.append(sys.stdin.readline().rstrip())

check(order, general.keys())
print("실행")

# if general_price < 20000 and special_price > 0:
#     print("No")
# elif (general_price + special_price) < 50000 and count > 0:
#     print("No")
# elif count > 1:
#     print("No")
# else:
#     print("Okay")
