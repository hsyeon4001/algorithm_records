# 24. Swap Nodes in Pairs
# 1) value 교환 => 24ms / 14MB
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        
        return head

# 2) swap 반복 => 40ms / 13.8MB
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
        
        return root.next

# 3) swap 재귀 => 324ms / 14.2MB
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            print(p, head.next, p.next)
            return p
    
        return head