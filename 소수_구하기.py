import sys

input = sys.stdin.readline

m, n = [int(x) for x in input().split()]

for i in range(m, n+1):
    if i < 2:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j==0: 
            break 
    else:
        print(i)