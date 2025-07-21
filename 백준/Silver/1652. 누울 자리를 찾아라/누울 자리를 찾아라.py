n = int(input())
nlist = [input() for _ in range(n)]
width = 0; height = 0

# 가로 방향
for string in nlist:
    dlist = [len(i) for i in string.split('X')]
    for num in dlist:
        if num >= 2:
            width += 1

# 세로 방향으로 회전
nlist = [list(i) for i in nlist]
rotate_arr = [['.']*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        rotate_arr[x][y] = nlist[n-1-y][x]

rotate_arr = [''.join(i) for i in rotate_arr]

# 세로 방향
for string in rotate_arr:
    dlist = [len(i) for i in string.split('X')]
    for num in dlist:
        if num >= 2:
            height += 1

print(width, height)