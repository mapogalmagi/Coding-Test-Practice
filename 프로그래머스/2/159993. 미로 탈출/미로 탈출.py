from collections import deque

def bfs(graph, queue, end):
    n = len(graph)
    m = len(graph[0])
    
    # 방문 여부
    visited = [[False]*m for _ in range(n)]
    
    # 상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    cost = 0
    
    while queue:
        x, y, cost = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            a, b = x+dx[i], y+dy[i]
            
            # end와 같으면 break
            if (a,b) == end:
                return cost
            if 0<=a<n and 0<=b<m and graph[a][b] != 'X':
                if not visited[a][b]:
                    visited[a][b] = True
                    queue.append((a,b,cost+1))
    return -1
            
def solution(maps):
    
    queue1 = deque([]) # 시작점 -> 레버
    queue2 = deque([]) # 레버 -> 도착점
    end1 = (0,0) # 도착점1 : 레버
    end2 = (0,0) # 도착점2 : 도착점
    
    # 시작점 설정
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                queue1.append((i,j,1))   # (좌표, 비용)
            if maps[i][j] == 'L':
                queue2.append((i,j,1))
                end1 = (i,j)
            if maps[i][j] == 'E':
                end2 = (i,j)
    
    a = bfs(maps, queue1, end1)
    b = bfs(maps, queue2, end2)
    
    if a != -1 and b != -1:
        return a + b
    else:
        return -1