from collections import defaultdict

def checkIfPrerequisite(numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    adj = defaultdict(list)
    for prereq, crs in prerequisites:
        adj[crs].append(prereq)

    def dfs(crs):
        if crs not in prereqMap:
            prereqMap[crs] = set()
            for prereq in adj[crs]:
                prereqMap[crs] |= dfs(prereq) # union
            prereqMap[crs].add(crs)
        return prereqMap[crs]

    prereqMap = {}
    for crs in range(numCourses):
        dfs(crs)

    res = []
    for u, v in queries:
        res.append(u in prereqMap[v])
    return res