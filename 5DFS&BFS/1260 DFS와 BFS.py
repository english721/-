n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    m1, m2 = map(int, input().split())
    # 노드 연결하기
    graph[m1][m2] = graph[m2][m1] = 1

# 깊이 우선 탐색
def dfs(v, visited=[]):
    visited.append(v)
    print(v, end = ' ')
    for i in range(len(graph[v])):
        # 1이라는 소리는 연결되어 있고, visited에 들어가 있지 않으면 재귀
        if graph[v][i] == 1 and (i not in visited):
            dfs(i, visited)

# 너비 우선 탐색
from collections import deque
def bfs(v):
    visited = [v]
    queue = deque()
    queue.append(v)
    while queue:
        vv = queue.popleft()
        print(vv, end = ' ')
        for i in range(len(graph[v])):
            if graph[vv][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)

dfs(v)
print()
bfs(v)