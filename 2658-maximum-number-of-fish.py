def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    N = len(edges)
    par = [i for i in range(N + 1)] # ith node -> parent (1 - n) [0 1 2 3 ...]
    rank = [1] * (N + 1) # ith node -> rank (1 - n)

    def find(n):
        if n != par[n]: # If `n` is not its own parent
            par[n] = find(par[n]) # Path compression (flatten the tree)
        return par[n]
    
    def union(n1, n2):
        p1, p2 = find(n1), find(n2) # Find root parents
        if p1 == p2:
            return False # `n1` and `n2` already connected → cycle detected
        
        if rank[p1] > rank[p2]: # Attach smaller tree to larger tree
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True
    
    for n1, n2 in edges:
        if not union(n1, n2): # If union() returns False (cycle detected)
            return [n1, n2] # Return the edge that caused the cycle