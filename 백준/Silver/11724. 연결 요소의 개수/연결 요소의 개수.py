#백준 - 연결 요소의 개수 -
import sys
from collections import deque

input = sys.stdin.readline

# 너비우선탐색 - 큐 사용 (덱)
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

#입력 
# 정점, 간선
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 방문처리는 정점의 수까지 (0제외니까 +1)

for _ in range(M):
    a, b = map(int, input().split())
    # 방향이 없기 때문에, 서로 크로스로 입력 해준다. 
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

print(count)