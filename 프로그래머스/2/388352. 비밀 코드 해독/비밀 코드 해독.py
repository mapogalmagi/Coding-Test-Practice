from itertools import combinations
def solution(n, q, ans):
    answer = 0
    
    for li in combinations([i for i in range(1,n+1)], 5):
        s = set(li); ok = 0
        
        for idx, nlist in enumerate(q):
            ss = set(nlist)
            if len(s&ss) == ans[idx]:
                ok += 1
            else:
                break
        
        if ok == len(q):
            answer += 1
    
    return answer