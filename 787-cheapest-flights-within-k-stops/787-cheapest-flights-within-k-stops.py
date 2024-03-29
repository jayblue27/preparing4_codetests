class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         #풀이 - 다익스트라 - 
#         graph = collections.defaultdict(list)
#         #그래프 인접 리스트 구성
#         for u,v,w in flights:
#             graph[u].append((v,w))
        
#         # 큐 변수: [(가격,정점,남은 가능 경유지 수)]
#         Q = [(0,  src, k)]
        
#         # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
#         while Q:
#             price, node, k = heapq.heappop(Q)
#             if node == dst:
#                 return price
#             if k >= 0:
#                 for v,w in graph[node]:
#                     alt = price+w
#                     heapq.heappush(Q,(alt,v,k-1))
#         return -1

        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1    