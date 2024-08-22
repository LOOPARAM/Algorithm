import sys
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)

sys.setrecursionlimit(100000)

M = 10
N = 100

table = [0] * (M + 1)
for i in range(0, M + 1):
    table[i] = [0] * (N + 1)
    table[i][0] = 1

for i in range(2, M + 1):  # 'pre'가 2 이상이므로 i는 2부터 시작합니다.
    for j in range(1, N + 1):
        if j >= i:
            table[i][j] = table[i][j - i] + table[i - 1][j]
        else:
            table[i][j] = table[i - 1][j]

print(table[M][N])
