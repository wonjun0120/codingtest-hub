import sys

input = sys.stdin.readline
n = int(input())

def recur(num, memo={}):
    if num in memo:
        return memo[num]
    
    if num <= 3:
        return num

    min_val = float('inf')
    for i in range(1, int(num ** 0.5) + 1):
        min_val = min(min_val, recur(num - i ** 2))
    
    memo[num] = min_val + 1
    return memo[num]

print(recur(n))
