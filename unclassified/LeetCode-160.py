# Definition for singly-linked list.
# 内存中指向的是同一个位置的才是交点，仅仅是数值相同的话，不算是交点的
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        if  not headA or not headB: # 有一个链表为空的话，就返回空置
            return None
        h_a = headA
        h_b = headB
        while h_a!= h_b: # 两者要是不相交，并且相等的话，一定最后会有返回值的，一定保证每一个都走了 a+b+c的距离
            if h_a.next == None and h_b.next == None: # 到达链表尾部了
                return None # 两者同时到达终点的情况 只有两种可能，一种是链表长度相等，一种是二者根本不相交,无论哪一种，都是不相交                
            elif h_b.next == None:
                h_b = headA
                h_a = h_a.next
            elif h_a.next == None:
                h_a = headB
                h_b = h_b.next
            else:
                h_a = h_a.next
                h_b = h_b.next
        
        return h_a
    
