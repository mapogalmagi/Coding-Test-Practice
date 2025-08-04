import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    # 엔터 무시용 변수
    disturb_enter = input()
    
    a, b = map(int, input().split())
    sejun = sorted(list(map(int, input().split())), reverse = True)
    sebi = sorted(list(map(int, input().split())), reverse = True)

    while sejun and sebi:
        if sejun[-1] < sebi[-1]:
            sejun.pop()
        else:
            sebi.pop()
    
    if not sejun:
        print('B')
    if not sebi:
        print('S')