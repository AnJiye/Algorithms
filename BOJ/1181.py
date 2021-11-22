# 1181번: 단어 정렬
n = int(input())

data = set()
for i in range(n):
    data.add(input())

# 먼저 알파벳 순으로 정렬
result = sorted(data)
# 그 후, 길이 순으로 정렬
result.sort(key=len)

for i in result:
    print(i)
