# 10809번: 알파벳 찾기
s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = [-1 for i in range(len(alphabet))]

for i in range(len(s)):
    index = alphabet.index(s[i])
    if result[index] == -1:
        result[index] = i

for i in range(len(result)):
    print(result[i], end=' ')

# s = input()
# alphabet = list(range(97, 123))

# for i in alphabet:
#     print(s.find(chr(i)), end=' ')
