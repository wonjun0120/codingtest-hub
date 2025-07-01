import sys

input = sys.stdin.readline
n = int(input())

staris = [int(input()) for _ in range(n)]

if len(staris) <= 2:
    print(sum(staris))

else:
    dp = [0 for _ in range(n)]
    dp[0] = staris[0]
    dp[1] = staris[0] + staris[1]

    for i in range(2,n): 
        dp[i] = max(dp[i-3] + staris[i-1] + staris[i], dp[i-2] + staris[i])
    print(dp[-1])