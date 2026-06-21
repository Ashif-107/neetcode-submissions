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
        while h1 and h2:
            cur = h1.val + h2.val + carry
            a = cur%10
            carry = cur//10
            res.next = ListNode(a)
            res = res.next
            
            h1 = h1.next
            h2 = h2.next
        
        while h1:
            cur = h1.val + carry
            a = cur%10
            carry = cur//10
            res.next = ListNode(a)
            res = res.next
            
            h1 = h1.next
        while h2:
            cur = h2.val + carry
            a = cur%10
            carry = cur//10
            res.next = ListNode(a)
            res = res.next
            
            h2 = h2.next
        
        if carry:
            res.next = ListNode(carry)

        return result.next
        
