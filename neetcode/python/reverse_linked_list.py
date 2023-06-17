"""
Given the head of a singly linked list, reverse the list, and return the
reversed list.

1 -> 2 -> 3 -> 4 -> 5
to
5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            current.next, prev, current = prev, current, current.next
        return prev


if __name__ == "__main__":
    a = ListNode(4, ListNode(5))
    b = ListNode(5, ListNode(4))
    c = Solution.reverseList(a)
    print(f"{b.val=}, {b.next.val=}")
    print(f"{c.val=}, {c.next.val=}")
