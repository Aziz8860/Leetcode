def isBalanced(self, root: Optional[TreeNode]) -> bool:
    balanced = [True]

    def height(root):
        if not root:
            return 0
        
        left_height = height(root.left)
        if balanced[0] is False:
            return 0
        
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            balanced[0] = False
            return 0
        
        return 1 + max(left_height, right_height)
    
    height(root)
    return balanced[0]

    # neetcode
    # def dfs(root):
    #     if not root: return [True, 0]

    #     left, right = dfs(root.left), dfs(root.right)
    #     balanced = (left[0] and right[0] and
    #                 abs(left[1] - right[1]) <= 1)
        
    #     return [balanced, 1 + max(left[1], right[1])]
    
    # return dfs(root)[0]