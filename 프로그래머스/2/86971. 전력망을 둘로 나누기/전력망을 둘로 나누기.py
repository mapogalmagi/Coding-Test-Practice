from collections import deque

def bfs(x, graph, visited):
    queue = deque([x])
    visited[x] = True
    cnt = 0
    
    while queue:
        cnt += 1
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
    return cnt
    

def solution(n, wires):
    answer = 1000000000
    graph = {i:[] for i in range(n+1)}
    
    # 그래프 기본 설정
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    for x, y in wires:
         # 그래프 복사 (deepcopy 대신 새 dict)
        mid = {key: value[:] for key, value in graph.items()}
        mid[x].remove(y)
        mid[y].remove(x)
        
        visited = [False]*(n+1)
        part_size = bfs(x, mid, visited)
        mid_answer = abs(part_size - (n - part_size))
        
        if answer > mid_answer:
            answer = mid_answer
        
    # 전체 node 수는 고정되어 있으므로 굳이 2개 구할 필요가 없다
    return answer