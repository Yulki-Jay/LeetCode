# Definition for singly-linked list.
# 最简单的思路，找到尾节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        new_head = ListNode(val=-1 , next=None) # 假设出一个哨兵节点
        cur = head
        while cur:
            tmp = ListNode(val=cur.val,next=new_head.next) # 注意了，python中等于号相当于起了一个别名！！！不申请新空间就出问题可还行
            # tmp = cur # 这么写的话，两个指针指的是一个东西，烦死了
            # tmp.next = new_head
            new_head.next = tmp
            cur = cur.next
        return new_head.next


L5 = ListNode(5,None)
L4 = ListNode(4,L5)
L3 = ListNode(3,L4)
L2 = ListNode(2,L3)
L1 = ListNode(1,L2)

s =Solution()
res = s.reverseList(L1)
while res:
    print(res.val)
    res = res.next

# a = 1
# print(a)
# b = a
# print(b)
# a = 2
# print(a)
# print(b)

