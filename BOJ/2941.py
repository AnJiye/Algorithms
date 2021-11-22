# 2941번: 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = [0 for i in range(len(croatia))]
word = input()

for i in range(len(croatia)):
    if croatia[i] in word:
        cnt[i] = word.count(croatia[i])
        word = word.replace(croatia[i], " ")    # 공백으로 사이 간격 대체 nljj 같은 경우를 대비

word = word.replace(" ", "")    # 공백 제거

print(sum(cnt)+len(word))


# 굳이 위처럼 안해도..
# for i in croatia:
#     word = word.replace(i, "*")

# print(len(word))
