# 2920번: 음계

data = list(input().split())

if data == sorted(data):
    print("ascending")
elif data == sorted(data, reverse=True):
    print("descending")
else:
    print("mixed")
