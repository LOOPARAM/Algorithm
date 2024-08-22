M = 10
N = 100

def check(remain,pre):
    
    if remain < 0:
        return 0
    elif remain == 0:
        return 1

    cnt = 0
    for i in range(pre,M+1):
        cnt += check(remain - i, i)
    return cnt

print(check(N,2))