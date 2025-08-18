from itertools import permutations

n = int(input())
nlist = list(map(int, input().split()))
answer = 0

for li in permutations(range(n), n):
    before = 0; mid_sum = 0
    sorted_nlist = [nlist[i] for i in li]
    # 절댓값 합 구하기
    for idx, num in enumerate(sorted_nlist):
        if idx == 0:
            before = num

        mid_sum += abs(before-num)
        before = num
        
    # 최댓값 찾기
    if answer < mid_sum:
        answer = mid_sum

print(answer)