from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = {i:[] for i in range(n+1)}
    for x,y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    dist = [-1]*(n+1)
    
    queue = deque([destination])
    dist[destination] = 0 # 자기 자신과의 거리 = 0
    
    while queue:
        v = queue.popleft()
        
        for node in graph[v]:
            if dist[node] == -1: # 아직 방문 안함
                dist[node] = dist[v] + 1
                queue.append(node)
                # queue가 돌면서 자연스레 dist가 커짐
    
    return [dist[s] for s in sources]