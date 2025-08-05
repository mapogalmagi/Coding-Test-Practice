from itertools import product

def solution(users, emoticons):
    price = [10, 20, 30, 40]
    answer = []
    
    for li in product(price, repeat = len(emoticons)):
        cnt = 0 # 플러스 산 사람 수
        entire_total = 0 # 플러스 안 사고 산 돈
        
        for user in users:
            total = 0
            for i in range(len(li)):
                # 할인율이 커서 사는 경우
                if user[0]<= li[i]:
                    total += emoticons[i]*(1-li[i]/100)
            
            if user[1] <= total:
                cnt += 1
            else:
                entire_total += total
        
        answer.append([cnt, entire_total])
    
    return sorted(answer, key = lambda x: (-x[0], -x[1]))[0]
                    