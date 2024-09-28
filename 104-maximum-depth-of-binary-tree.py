from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Recursive
    if not root:
        return 0
    
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return 1 + max(left, right)

    # BFS (basically traversal)
    # if not root:
    #     return 0
    # level = 0
    # q = deque([root])
    # while q:
    #     for i in range(len(q)):
    #         root = q.popleft()
    #         if root.left:
    #             q.append(root.left)
    #         if node.right:
    #             q.append(root.right)
    #     level += 1
    # return level

    # Iterative DFS
    # stack = [[root, 1]]
    # res = 0
    # while stack:
    #     node, depth = stack.pop()
    #     if node:
    #         res = max(res, depth)
    #         stack.append([node.left, depth + 1])
    #         stack.append([node.right, depth + 1])
    # return res