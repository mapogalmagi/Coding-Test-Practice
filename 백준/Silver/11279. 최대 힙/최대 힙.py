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
            # heappush를 마이너스 값을 넣어 최대힙을 생성했으므로
            # 실제로 값을 뽑을때는 마이너스 붙여서 나와야 원래 값 출력
            print(-1*heapq.heappop(heap))
    else:
        heapq.heappush(heap, -s)    