def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # recursive method
    # res = []
    # def inorder(root):
    #     if not root:
    #         return
    #     inorder(root.left)
    #     res.append(root.val)
    #     inorder(root.right)
    # inorder(root)
    # return res

    # iterative method
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res