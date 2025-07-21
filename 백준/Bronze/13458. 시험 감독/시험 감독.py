import sys

input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
x, y = map(int, input().split())

answer = 0

for num in nlist:
    if num <= x:
        answer += 1
    else:
        num -= x
        if num % y == 0:
            answer += num // y + 1
        else:
            answer += num // y + 2
print(answer)   