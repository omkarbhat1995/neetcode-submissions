# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # Move both pointers until right reaches the end
        while right:
            left = left.next # pyright: ignore[reportOptionalMemberAccess]
            right = right.next
            
        # Delete the nth node
        left.next = left.next.next # pyright: ignore[reportOptionalMemberAccess]
        
        return dummy.next