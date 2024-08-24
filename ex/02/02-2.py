memo = {}
memo[0] = 1

def factorial(n):
    global memo 
    if n in memo:
        return memo[n]
    memo[n] = n * factorial(n-1)
    return memo[n]

def nCr(n,r):
    return factorial(n) / (factorial(r)*factorial(n-r))

print(nCr(10,3))