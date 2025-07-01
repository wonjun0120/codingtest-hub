import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    x, y = [int(x) for x in input().strip().split()]
    li.append([x, y])

li.sort(key=lambda x : (x[0], x[1]))

for el in li:
    print(' '.join([str(x) for x in el]))