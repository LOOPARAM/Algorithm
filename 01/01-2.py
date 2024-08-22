import sys
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)

sys.setrecursionlimit(100000)

M = 10
N = 100

memo = {}
def check(remain,pre):
    
    key = str([remain,pre])
    if key in memo:
        return memo[key]

    if remain < 0:
        return 0
    elif remain == 0:
        return 1

    cnt = 0
    for i in range(pre,M+1):
        cnt += check(remain - i, i)

    memo[key] = cnt
    return cnt

print(check(N,2))