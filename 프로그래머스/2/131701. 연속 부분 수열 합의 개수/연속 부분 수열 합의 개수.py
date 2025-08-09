def solution(elements):
    n = len(elements)     # 기본 element 길이 저장
    arr = elements * 2    # 원형 수열 처리용
    arr_set = set()
    
    for i in range(1,n+1):
        s = sum(arr[0:i])  # 길이가 1~n인 수열의 합
        arr_set.add(s)
        for j in range(1,n): # 원순열이라 n-1까지만 돌려도 ㅇㅋ
            s += arr[i+j-1]
            s -= arr[j]
            arr_set.add(s)
    
    return len(arr_set)