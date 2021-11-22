# 1427번: 소트인사이드

n = input()
result = sorted(n, reverse=True)
for i in result:
    print(i, end='')
