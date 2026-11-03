# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        if size == n:
            return head.next

        index = 0
        curr = head
        prev = None
        while curr:
            if index == (size - n):
                prev.next = curr.next
                curr.next = None
                break

            index += 1
            prev = curr
            curr = curr.next

        return head