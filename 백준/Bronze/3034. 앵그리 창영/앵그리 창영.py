n, w, h = map(int, input().split())

comp = w ** 2 + h ** 2

for _ in range(n):
    num = int(input())
    if comp >= num ** 2:
        print('DA')
    else:
        print('NE')