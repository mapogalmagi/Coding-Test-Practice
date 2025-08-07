def solution(N, K):
    lo, hi = 1, K
    answer = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        # mid 이하인 수가 몇 개인지 세기
        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)

        if count >= K:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return answer

# 입력 처리
N = int(input())
K = int(input())
print(solution(N, K))
