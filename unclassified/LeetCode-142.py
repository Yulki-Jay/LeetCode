# Definition for singly-linked list.
# 判断两个链表是否有环，有环的话，需要找到环的位置
# 双指针的思想，快指针先走，每次走两步，如果走的时候就遇见了None，则说明这个链表没有环
# 如果快指针和慢指针相遇了，则记录一下相遇的那一个点，两个指针一个回到表头，一个接着从这里走
# 再次相遇的时候就是，就是环的入口的位置
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head: # 没有节点的情况
            return None
        fast = head  # 都从表头开始走
        slow = head
        count = 0  # 第一次最开始的时候指定都指向了一个点，所以要处理一下第一次的点
        while True:
            if fast.next!=None:
                fast = fast.next
                if fast.next!=None:
                    fast = fast.next
                else:
                    return None # 不能走两步
            else:
                return None # 甚至fast下一步都没有
            slow = slow.next
            if slow == fast:
                break
        # 到这里slow和fast已经相遇了
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next    
        return slow # 这就是最后相遇的点