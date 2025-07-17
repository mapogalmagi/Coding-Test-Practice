import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    s = int(input())

    if s == 0:
        # heap이 비어있는 경우
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(s), s))    