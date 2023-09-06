# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        # 假设出一个哨兵节点
        h = ListNode(val=-1,next=head)
        if h.next ==None or h.next.next ==None:
            return head  
        # 上述处理了 链表为空 或者链表只有一个节点的情况
        pre = h
        cur = head
        pt = head.next
        tmp = ListNode(val=-1,next=None)
        while cur:
            tmp = pt.next
            pt.next = cur
            cur.next = tmp
            pre.next = pt
            
            cur = cur.next # 可以保证cur一直在奇数点的位置
            if not cur:
                return h.next
            if cur.next:
                pre = pt.next
                pt =cur.next
            else:
                return h.next
                    
L4 = ListNode(4,None)       
L3 = ListNode(3,L4)       
L2 = ListNode(2,L3)      
L1 = ListNode(1,None)    
L0 = None   
        
        
s = Solution()
res = s.swapPairs(L0)
while res:
    print(res.val)
    res = res.next
        