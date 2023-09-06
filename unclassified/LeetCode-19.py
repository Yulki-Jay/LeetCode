# Definition for singly-linked list.
# 删除倒数第n个节点，只要等到出发了n个之后再出发就好了，不保存前一个指针，直接交换值
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        h = ListNode(-1,head)
        cur = head
        prr = h
        pr = head
        while cur.next: # 一定要注意这里，如果不是next的话，会多移动一次，造成pr指的是cur，prr指的是应该被删除的元素
            count += 1
            if count >= n: # 检查一下这里是不是对的
                pr = pr.next
                prr = prr.next
            cur = cur.next
        # 找到之后,有可能删除最后一个节点
        prr.next = pr.next
        return h.next

L5 = ListNode(5,None)
L4 = ListNode(4,L5)       
L3 = ListNode(3,L4)       
L2 = ListNode(2,L3)      
L1 = ListNode(1,L2)  

s = Solution()
res = s.removeNthFromEnd(L1,2)
while res:
    print(res.val)
    res = res.next