import heapq

max_heap = []
min_heap = []
latest = dict()  # 문제번호 → 최신 난이도

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    heapq.heappush(max_heap, (-b, -a))
    heapq.heappush(min_heap, (b, a))
    latest[a] = b  # 현재 난이도 저장

n = int(input())
for _ in range(n):
    slist = input().split()
    execute = slist[0]

    if execute == 'add':
        a, b = int(slist[1]), int(slist[2])
        heapq.heappush(max_heap, (-b, -a))
        heapq.heappush(min_heap, (b, a))
        latest[a] = b  # 최신 값 갱신

    elif execute == 'solved':
        a = int(slist[1])
        if a in latest:
            del latest[a]  # 삭제 표시

    elif execute == 'recommend':
        if slist[1] == '1':
            while True:
                lv, num = heapq.heappop(max_heap)
                lv, num = -lv, -num
                if latest.get(num) == lv:
                    print(num)
                    heapq.heappush(max_heap, (-lv, -num))  # 복구
                    break
        elif slist[1] == '-1':
            while True:
                lv, num = heapq.heappop(min_heap)
                if latest.get(num) == lv:
                    print(num)
                    heapq.heappush(min_heap, (lv, num))  # 복구
                    break
