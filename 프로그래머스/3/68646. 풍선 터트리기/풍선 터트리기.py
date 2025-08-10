def solution(a):
    answer = 2
    
    left_sorted_min = []
    right_sorted_min = []
    left_min, right_min = 1_000_000_001,1_000_000_001 
    
    if len(a) <= 2:
        return len(a)
    
    for num in a:
        if num < left_min:
            left_min = num
        left_sorted_min.append(left_min)
    
    # 오른쪽에서 데이터를 삭제하려고 하지말고
    # 처음부터 최솟값을 저장해놓으면 그냥 꺼내 쓰기만 하면 된다 (O(1))
    for num in a[::-1]:
        if num < right_min:
            right_min = num
        right_sorted_min.append(right_min)
    
    for i in range(1, len(a)-1):
        if a[i] <= left_sorted_min[i-1] or a[i] <= right_sorted_min[len(a)-2-i]:
            answer += 1
        
    return answer