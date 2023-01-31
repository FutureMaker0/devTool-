INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 거리값 입력받음
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 점화식 수행 - 3중 for 문
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 결과 출력부
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, "무한"이라고 출력.
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print(' ')