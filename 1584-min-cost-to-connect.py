import heapq

def minCostConnectPoints(self, points: List[List[int]]) -> int:
    heap = []
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            distance = abs(xi - xj) + abs(yi - yj)
            heapq.heappush(heap, (distance, i, j))

    parent = list(range(n))
    rank = [1] * n
    
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

    edges_used = 0
    total_dist = 0
    while heap:
        distance, i, j = heap.heappop(heap)

        if union(i, j):
            edges_used += 1
            total_dist += distance
        
        if edges_used == n - 1:
            return total_dist
        
    return total_dist