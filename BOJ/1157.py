# 1157번: 단어 공부
s = input().upper()
unique = list(set(s))
cnt = []

for i in unique:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max_index = cnt.index(max(cnt))
    print(unique[max_index])
