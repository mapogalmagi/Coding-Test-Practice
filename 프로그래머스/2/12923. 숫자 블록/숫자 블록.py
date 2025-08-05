def solution(begin, end):
    answer = []
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue
        
        block = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                # num = i * (num // i)
                # 조건에서 블럭은 10000000개 이하로 존재한다고 되어있음
                # (i, num//i) 중에 블럭 100000000개 
                if num // i <= 10_000_000:
                    block = num // i
                    break
                # i ≤ 10,000,000이면 그게 ‘사용 가능한 가장 큰 약수’
                elif i <= 10_000_000:
                    block = i
        answer.append(block)
    return answer