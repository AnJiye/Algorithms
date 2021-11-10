# 위에서 아래로

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

# print(array)

for i in array:
    print(i, end=' ')

# for i in range(n):
#     print(array[i], end=' ')
