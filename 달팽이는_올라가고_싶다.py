import sys
import math
input = sys.stdin.readline

a, b, v = [int(x) for x in input().split(' ')]

print((math.ceil((v - b) / (a - b))))