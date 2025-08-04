from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
answer = 0

chick_list = [list(map(int, input().split())) for _ in range(n)]

for i, j, k in combinations(range(m), 3):
    total = 0
    for num in range(n):
        total += max(chick_list[num][i], chick_list[num][j], chick_list[num][k])
                     
    if answer < total:
        answer = total

print(answer)