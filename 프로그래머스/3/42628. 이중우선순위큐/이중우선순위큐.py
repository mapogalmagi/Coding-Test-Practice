import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = dict()
    idx = 0  # 고유 ID

    for op in operations:
        if op.startswith('I'):
            num = int(op.split()[1])
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
            idx += 1

        elif op == "D 1":
            # 최대값 삭제
            while max_heap:
                value, i = heapq.heappop(max_heap)
                if visited[i]:
                    visited[i] = False
                    break

        elif op == "D -1":
            # 최소값 삭제
            while min_heap:
                value, i = heapq.heappop(min_heap)
                if visited[i]:
                    visited[i] = False
                    break

    # 남아있는 유효한 값만 찾기
    max_val = None
    while max_heap:
        value, i = heapq.heappop(max_heap)
        if visited[i]:
            max_val = -value
            break

    min_val = None
    while min_heap:
        value, i = heapq.heappop(min_heap)
        if visited[i]:
            min_val = value
            break

    if max_val is None or min_val is None:
        return [0, 0]
    return [max_val, min_val]