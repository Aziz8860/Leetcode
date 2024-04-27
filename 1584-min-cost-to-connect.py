import heapq

def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # Building the heap with all possible edges based on the Manhattan distance
    heap = []
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            distance = abs(xi - xj) + abs(yi - yj)
            heapq.heappush(heap, (distance, i, j))

    # Disjoint set (Union-Find) initialization
    parent = list(range(n))
    rank = [1] * n  # Using rank to keep track of the depth of trees
    
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x == root_y: return False
        if rank[y] < rank[x]:
            parent[root_y] = root_x
            rank[root_x] += rank[root_y]
        else:
            parent[root_x] = root_y
            rank[root_y] += rank[root_x]
        
        return True

    # Kruskal's algorithm to construct the minimum spanning tree (MST)
    edges_used = 0
    total_dist = 0
    while heap:
        distance, i, j = heap.heappop(heap)

        if union(i, j):
            edges_used += 1
            total_dist += distance
        
        if edges_used == n - 1:
            return total_dist
    
    # The minimum cost to connect all points
    return total_dist


    # neetcode's solution
    # buat adjacency list
    # N = len(points)

    # adj = {i:[] for i in range(N)} # i : list of [cost, node]

    # for i in range(N):
    #     x1, y1 = points[i]
    #     for j in range(i + 1, N):
    #         x2, y2 = points[j]
    #         dist = abs(x1 - x2) + abs(y1 - y2) # manhattan
    #         adj[i].append([dist, j])
    #         adj[j].append([dist, i])
    
    # # Prim's
    # res = 0
    # visit = set()
    # minH = [[0, 0]] # [cost, point]
    # while len(visit) < N:
    #     cost, i = heapq.heappop(minH)
    #     if i in visit:
    #         continue
    #     res += cost
    #     visit.add(i)
    #     for neiCost, nei in adj[i]:
    #         if nei not in visit:
    #             heapq.heappush(minH, [neiCost, nei])
    # return res
