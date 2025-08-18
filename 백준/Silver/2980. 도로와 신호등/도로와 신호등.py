wait_second = 0

N, L = map(int, input().split())
for _ in range(N):
    a, b, c = map(int, input().split())

    # 대기하면, 대기 시간 plus
    # a + wait_second : 여태까지 온 시간
    if (a + wait_second) % (b+c) < b:
        wait_second += b - (a + wait_second) % (b+c)

print(wait_second+L)