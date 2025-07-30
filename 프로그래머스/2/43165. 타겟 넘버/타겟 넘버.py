def solution(numbers, target):
    answer = []
    for idx, num in enumerate(numbers):
        mid = []
        
        if idx == 0:
            answer.append(num)
            answer.append(-1*num)
            continue
        
        for n in answer:
            mid.append(n+num)
            mid.append(n-num)
        
        answer = mid
        
    return answer.count(target)