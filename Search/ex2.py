# 정렬된 배열에서 특정 수의 개수 구하기 (367p)

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))


def count(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    if (right_index - left_index == 0):
        return -1
    return right_index - left_index


print(count(array, x, x))
