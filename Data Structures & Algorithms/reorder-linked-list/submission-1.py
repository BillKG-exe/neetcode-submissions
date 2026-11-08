# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        l2 = slow.next
        slow.next = None

        while l2:
            nex = l2.next
            l2.next = prev
            prev = l2
            l2 = nex

        l1 = head
        l2 = prev

        while l2:
            nex1, nex2 = l1.next, l2.next
            l1.next = l2
            l2.next = nex1
            l1 = nex1
            l2 = nex2


    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     stack = []

    #     curr = head
    #     while curr:
    #         stack.append(curr)
    #         curr = curr.next

    #     curr = head

    #     for _ in range(len(stack) // 2):
    #         nex = curr.next
    #         node = stack.pop()

    #         curr.next = node
    #         node.next = nex

    #         curr = nex

    #     curr.next = None