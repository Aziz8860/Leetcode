class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # if one child is None, return the depth of the other child
        if not root.left:
            return right + 1
        if not root.right:
            return left + 1

        # both children exist, so return the minimum depth
        return min(left, right) + 1