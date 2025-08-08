def solution(players, m, k):
    answer = 0
    server_list = []
    cnt = 0 # 현재 서버 수
    
    for idx, num in enumerate(players):
        # 감당 안 될때
        if num // m > cnt:
            mid = num // m - cnt # 증설된 서버 수
            cnt += mid
            answer += mid
            # 시작 위치, 지속 시간, 지금 서버 수
            server_list.append([idx,k, mid])
        
        # 기본 경우
        if server_list:
            # 시간이 경과함에 따라 감소
            for li in server_list:
                li[1] -= 1
        
        for li in server_list:
            if li[1] == 0:
                cnt -= li[2]
                
    return answer