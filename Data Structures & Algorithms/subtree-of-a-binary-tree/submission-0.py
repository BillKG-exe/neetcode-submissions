# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True

            if (not root1 and root2) or (not root2 and root1):
                return False

            if root1.val != root2.val:
                return False

            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        from collections import deque

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                break

            if isSameTree(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False