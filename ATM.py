import sys
input = sys.stdin.readline

n = int(input())

waits = list(map(int, input().split()))
waits.sort()

times = []
for i in range(len(waits)):
    times.append(sum(waits[:i + 1]))

print(sum(times))

