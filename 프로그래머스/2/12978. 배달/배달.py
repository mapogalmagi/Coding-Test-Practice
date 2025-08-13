import heapq
import math

# 1번 마을에서 각 마을에 도달하는 최소 시간(가중치 On) : 다익스트라
def solution(N, road, K):
    INF = 10000000000000000
    dist = [INF]*(N+1)
    
    # graph
    graph = [[] for _ in range(N+1)]
    for li in road:
        graph[li[0]].append((li[2],li[1])) # (비용, 목적지)
        graph[li[1]].append((li[2],li[0])) # 양방향
    
    # 시작점 초기화
    dist[1] = 0
    heap = [(0,1)]
    
    while heap:
        cur_w, cur_v = heapq.heappop(heap)
        
        if dist[cur_v]!= cur_w:
            continue
        
        for next_w, next_v in graph[cur_v]:
            # 기존보다 새로운 애가 작으면 갱신
            if dist[next_v] > cur_w + next_w:
                dist[next_v] = cur_w + next_w
                heapq.heappush(heap, (cur_w+next_w, next_v))
    
    return len([i for i in dist[1:] if i<=K])