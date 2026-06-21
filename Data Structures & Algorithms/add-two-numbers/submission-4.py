# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2 = l1,l2
        result = ListNode(0)
        res = result
        carry = 0
        while h1 or h2:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            cur = v1 + v2 + carry
            a = cur%10
            carry = cur//10
            res.next = ListNode(a)
            res = res.next
            
            if h1:
                h1 = h1.next

            if h2:
                h2 = h2.next

        
        
        if carry:
            res.next = ListNode(carry)

        return result.next
        
