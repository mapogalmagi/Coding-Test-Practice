from itertools import combinations

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    answer = []
    
    # 열의 개수 idx
    for idx in range(1,col_len + 1):
        # combination 앞에 들어가는 것은 iter 변수
        for cols in combinations(range(col_len), idx):
            # 유일성 검사
            projection = [tuple(arr[i] for i in cols) for arr in relation]
            if len(set(projection)) < row_len:
                continue
            # 리스트 전체가 같다고 검사하기 보다, 개수만 확인하면 상관 무!
            
            # 최소성 검사
            is_minimal = True
            for key in answer:
                if set(key).issubset(cols):
                    is_minimal = False
                    break
            
            if is_minimal:
                answer.append(cols)

    return len(answer)