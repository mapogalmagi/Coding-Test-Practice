from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # b가 해킹당하면 a도 해킹됨

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

max_count = 0
result = []

for i in range(1, n+1):
    count = bfs(i)
    if count > max_count:
        result = [i]
        max_count = count
    elif count == max_count:
        result.append(i)

print(*result)