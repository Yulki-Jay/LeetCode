# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        pt = ListNode()
        cur = head # 当前指针
        pt = head # 下一个指针
        while cur != None:
            next = cur.next
            while pt.val == cur.val:
                pt = pt.next
                if pt == None:
                    break
            cur.next = pt
            cur = pt
        return head
    
solution = Solution()
