def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    if s % n == 0:
        return [s//n] * n
    
    num = s % n; i = n-1
    answer = [s//n] * n
    while num > 0:
        answer[i] += 1
        num -= 1
        i -= 1
    
    return answer