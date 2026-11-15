class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            diameter = max(diameter, left_len + right_len)

            return 1 + max(left_len, right_len)

        dfs(root)
        return diameter