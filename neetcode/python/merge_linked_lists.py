"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    """
    Merge the two lists in a one sorted list. The list should be made by
    splicing together the nodes of the first two lists.
    """

    @staticmethod
    def mergeTwoLists(
        list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """Merge two sorted linked lists"""
        holder = ListNode()  # hold our place
        output = holder
        while list1 and list2:
            if list1.val < list2.val:
                output.next = list1
                list1 = list1.next
            elif list2:
                output.next = list2
                list2 = list2.next
            output = output.next
        # Add remainder to merged list
        if list1:
            output.next = list1
        elif list2:
            output.next = list2
        return holder.next
