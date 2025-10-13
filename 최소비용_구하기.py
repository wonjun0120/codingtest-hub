import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

# 인접 리스트로 변경
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, cost = map(int, input().strip().split())
    graph[u].append((v, cost))

# 출발 도시, 도착 도시
start, end = map(int, input().strip().split())

# 다익스트라 알고리즘
INF = float('inf')
min_cost = [INF] * (N + 1)
min_cost[start] = 0

# 우선순위 큐: (비용, 도시)
hq = [(0, start)]

while hq:
    cur_cost, cur_city = heapq.heappop(hq)

    # 이미 더 짧은 경로로 방문한 적 있으면 무시
    if min_cost[cur_city] < cur_cost:
        continue

    for next_city, cost in graph[cur_city]:
        new_cost = cur_cost + cost
        if new_cost < min_cost[next_city]:
            min_cost[next_city] = new_cost
            heapq.heappush(hq, (new_cost, next_city))

print(min_cost[end])
