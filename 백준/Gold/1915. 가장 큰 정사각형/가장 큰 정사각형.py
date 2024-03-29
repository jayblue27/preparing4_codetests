y, x = map(int, input().split())
graph = []
for _ in range(y):
    graph.append(list(map(int, list(input()))))
result = 0

for i in range(y):
    for j in range(x):
        if i > 0 and j > 0 and graph[i][j] == 1:
            graph[i][j] += min(graph[i][j-1], graph[i-1][j], graph[i-1][j-1])
        result = max(result, graph[i][j])
print(result**2)