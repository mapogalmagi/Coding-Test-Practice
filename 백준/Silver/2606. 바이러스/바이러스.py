import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 연결되어있으므로 각 노드에 대해 동시에 append
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

# 1번 컴퓨터에서 출발
dfs(1)

# 자기 자신은 제외
print(visited.count(True) - 1)