# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1

        idx = l - n
        start = head

        if idx == 0:
            return head.next
            
        for _ in range(idx-1):
            start = start.next
        
        start.next = start.next.next

        return head