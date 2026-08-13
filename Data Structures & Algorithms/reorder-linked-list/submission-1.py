# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        second = slow.next
        slow.next = None
        while second:
            currNext = second.next
            second.next = prev
            prev = second
            second = currNext

        while prev:
            temp1, temp2 = head.next, prev.next
            head.next, prev.next = prev, head.next
            prev = temp2
            head = temp1
