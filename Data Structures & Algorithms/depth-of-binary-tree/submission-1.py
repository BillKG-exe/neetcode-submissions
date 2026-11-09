# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0

    #     from collections import deque

    #     max_depth = 0
    #     queue = deque([root])
    #     while queue:
    #         level_size = len(queue)
    #         for i in range(level_size):
    #             node = queue.popleft()
    #             if not node: return

    #             if node.left:
    #                 queue.append(node.left)

    #             if node.right:
    #                 queue.append(node.right)
            
    #         max_depth += 1
    #     return max_depth