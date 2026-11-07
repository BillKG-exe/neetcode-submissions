# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head

        for _ in range(len(stack) // 2):
            nex = curr.next
            node = stack.pop()

            curr.next = node
            node.next = nex

            curr = nex

        curr.next = None