# 92. Reverse Linked List II
# 1) 노드 뒤집기 반복 => 28ms / 14.2MB
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head

        for _ in range(m-1):
            start = start.next
        end = start.next
        
        for _ in range(n-m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next