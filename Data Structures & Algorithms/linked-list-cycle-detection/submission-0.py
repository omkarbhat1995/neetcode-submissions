# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # type: ignore # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they meet, a cycle exists
            if slow == fast:
                return True
                
        # If fast reaches the end, there is no cycle
        return False