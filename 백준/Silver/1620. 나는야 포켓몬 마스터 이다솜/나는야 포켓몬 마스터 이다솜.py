a_dic = {}; b_dic = {}

n, m = map(int, input().split())

for idx in range(n):
    s = input()
    a_dic[str(idx+1)] = s
    b_dic[s] = str(idx+1)

for _ in range(m):
    ss = input()
    if ss.isdigit():
        print(a_dic[ss])
    else:
        print(b_dic[ss])