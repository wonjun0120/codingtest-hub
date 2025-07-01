import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
a.sort(reverse=True)

answer = sum(a[i] * b[i] for i in range(n))

print(answer)