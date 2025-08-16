def solution(routes):
    if not routes:
        return 0
    routes.sort(key=lambda x: x[1])  # 종료 지점 오름차순
    camera = routes[0][1]
    answer = 1
    for s, e in routes[1:]:
        if s > camera:          
            answer += 1
            camera = e          
    return answer