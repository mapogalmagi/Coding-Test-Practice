from math import ceil

n = int(input())
m = int(input())
numlist = list(map(int, input().split()))

distances = [numlist[0]] + \
            [ceil((numlist[i] - numlist[i-1]) / 2) for i in range(1, m)] + \
            [n - numlist[-1]]

print(max(distances))