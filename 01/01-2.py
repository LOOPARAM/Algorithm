#n명의 사람이 있을 때, 한번에 승리자가 결정될 수 있는 조합은 몇가지?
#4명 -> 12가지

def rsp(n):
    count = 0
    for r in range(0,n+1):
        for s in range(0,n-r+1):
            p = 4 - r - s
            all = [r,s,p]
            if all.count(max(all))==1 :
                count+=1
    return count

print(rsp(100))