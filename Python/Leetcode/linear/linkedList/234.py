# 234. Palindrome Linked List
# 1) 리스트 변환 => 164ms / 24.1MB
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:+

        q: List = []

        if not head:
            return True
        
        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

# 2) 이중 연결 리스트 => 64ms / 23.8MB
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True
        
        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True

# 3) 러너 => 64ms / 24MB
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev
