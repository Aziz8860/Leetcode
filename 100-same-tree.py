# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def same(p, q):
        if not p and not q: # structurally same
            return True
        
        # sama aja: if not p or not q
        if (p and not q) or (q and not p): # structurally different
            return False
        
        if p.val != q.val:
            return False
        
        return same(p.left, q.left) and same(p.right, q.right)
    
    return same(p, q)
    # Time: O(n + m)
    # Space: O(h_p + h_q)