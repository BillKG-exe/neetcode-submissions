# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        sorted_list = None
        index = None

        while curr1 and curr2:
            if curr1.val < curr2.val:
                if not sorted_list:
                    sorted_list = curr1
                    index = sorted_list
                else:
                    index.next = curr1
                    index = index.next

                curr1 = curr1.next
            else:
                if not sorted_list:
                    sorted_list = curr2
                    index = sorted_list
                else:
                    index.next = curr2
                    index = index.next

                curr2 = curr2.next

        while curr1:
            index.next = curr1
            index = index.next
            curr1 = curr1.next

        while curr2:
            index.next = curr2
            index = index.next
            curr2 = curr2.next

        return sorted_list

                    