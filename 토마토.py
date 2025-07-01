# 토마토 7576
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # 열, 행

store = []
queue = deque()
unripe_count = 0

for n in range(N):
    row = list(map(int, input().split()))
    for m, val in enumerate(row):
        if val == 1:
            queue.append((n, m, 0))  # (행, 열, 시간)
        elif val == 0:
            unripe_count += 1
    store.append(row)

# 모든 토마토가 익어있다면
if unripe_count == 0:
    print(0)
    sys.exit(0)

answer = 0
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

while queue:
    cn, cm, time = queue.popleft()
    for i in range(4):
        nn, nm = cn + dn[i], cm + dm[i]
        if 0 <= nn < N and 0 <= nm < M:
            if store[nn][nm] == 0:
                store[nn][nm] = 1
                unripe_count -= 1
                queue.append((nn, nm, time + 1))
                answer = max(answer, time + 1)

# 다 익지 못한 토마토가 있다면
if unripe_count > 0:
    print(-1)
else:
    print(answer)




# 토마토 7569
# import sys
# import collections

# input = sys.stdin.readline

# M, N, H = map(int, input().split())

# stores = []
# stack = collections.deque([])

# is_complete = True
# for h in range(H):
#     layer = []
#     for n in range(N):
#         li = list(input().strip().split())
#         for m, el in enumerate(li):
#             if el == '1': stack.append((h, n, m, 0))
#             if el == '0': is_complete = False

#         layer.append(li)
        

#     stores.append(layer)

# if len(stack) < 1:
#     print(-1)

# if is_complete: 
#     print(0)

# else:
#     answer = -1
#     while stack:
#         ch, cn, cm, time = stack.popleft()

#         for dh, dn, dm in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
#             nh = dh + ch
#             nn = dn + cn
#             nm = dm + cm

#             if nh < 0 or nh >= H: continue
#             if nn < 0 or nn >= N: continue
#             if nm < 0 or nm >= M: continue

#             if stores[nh][nn][nm] == '-1': continue
#             if stores[nh][nn][nm] == '1': continue
#             if stores[nh][nn][nm] == '0': 
#                 answer = max(answer, time+1)
#                 stores[nh][nn][nm] = '1'
#                 stack.append((nh, nn, nm, time+1))

#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 if stores[h][n][m] == '0':
#                     print(-1)
#                     sys.exit(0)

#     print(answer)

            

