## 기본적으로 플로이드 워셜 보다는 다익스트라가 훨씬 어려운 알고리즘으로 분류된다.
## 우선순위 큐를 이용한 다익스트라 알고리즘 작성

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n,m,start = map(int, input().split())

graph = [[] for _ in range(n+1)] # 그래프를 위한 배열 생성
distance = [INF] * (n+1) # 최단거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z)) # x노드에서 y노드로 가는 간선의 값이 z라는 의미

def djikstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(start)

# 도달할 수 있는 노드의 갯수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)


# 시작 노드는 제외해야하므로 count-1을 출력
print(count-1, max_distance)


'''
다익스트라는 정말 진짜 모르겠다...
'''