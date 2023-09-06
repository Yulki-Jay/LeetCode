# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int) :
        h = ListNode(val=0,next=head) # 构造一个包含头节点的链表
        pre = h
        cur = pre.next # pre 是前一个指针 cur 是当前指针
        while cur!=None:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur =cur.next
        return h.next     
s = Solution()                
head = []
val = 0

l7 = ListNode(val=6,next=None)
l6 = ListNode(val=5,next=l7)
l5 = ListNode(val=4,next=l6)
l4 = ListNode(val=3,next=l5)
l3 = ListNode(val=6,next=l4)
l2 = ListNode(val=2,next=l3)
l1 = ListNode(val=1,next=l2)

head = None



res = s.removeElements(head,val)
while res:
    print(res.val)
    res = res.next
            
        
    
    
