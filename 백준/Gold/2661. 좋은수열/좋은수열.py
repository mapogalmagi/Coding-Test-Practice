n = int(input())

def is_good(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        if s[-i:] == s[-2*i:-i]:
            return False
    return True

def dfs(s):
    if len(s) == n:
        print(s)
        exit()  # 첫 번째 정답을 찾으면 바로 종료 (사전순 보장)
    
    for num in '123':
        if is_good(s + num):
            dfs(s + num)

dfs('')
