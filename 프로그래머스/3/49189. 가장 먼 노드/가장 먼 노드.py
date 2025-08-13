from collections import deque

def solution(n, edge):
    # 1) 그래프 만들기 (1..n)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 2) 거리 배열: -1은 미방문
    dist = [-1] * (n + 1)
    dist[1] = 0

    # 3) BFS
    q = deque([1])
    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1
                q.append(nxt)

    # 4) 최댓값 개수 세기 (노드 1 제외는 어차피 거리 0이므로 영향 없음)
    far = max(dist[1:])          # 1번부터 n번까지 중 최댓값
    return sum(1 for d in dist if d == far)