class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = LinkNode(-1, next=None)
        self.length = 0
        
                
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        tmp = self.head
        count = -1
        while tmp and count<index:
            tmp = tmp.next
            count += 1
        return tmp.val if count==index else -1

    def addAtHead(self, val: int) -> None:
        tmp = LinkNode(val,next=None)
        tmp.next = self.head.next
        self.head.next = tmp
        self.length +=1

    def addAtTail(self, val: int) -> None:
        tmp = LinkNode(val,None)
        cur = self.head
        pre = cur
        while cur:
            pre = cur
            cur = cur.next    
        pre.next = tmp
        self.length +=1

    # 在index 位置添加节点
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            return self.addAtHead(val)
        elif index == self.length:
            return self.addAtTail(val)
        elif index > self.length:
            return
        else:
            tmp = LinkNode(val,None) # 新建的节点
            cur = self.head
            pre = cur
            count = -1
            while cur and count < index:
                pre = cur
                cur = cur.next
                count +=1
            if cur:
                tmp.next = cur
                pre.next = tmp
                self.length += 1 
        
        
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index >=self.length:
            return
        cur = self.head
        pre = cur
        count = -1
        while cur and count < index:
            pre = cur
            cur = cur.next
            count +=1
        if count == index:
            pre.next = cur.next
            self.length -= 1

        



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(5)
obj.addAtTail(6)
tmp = obj.head.next
obj.addAtIndex(1,4)
obj.deleteAtIndex(2)

param_1 = obj.get(2)

while tmp:
    print(tmp.val)
    tmp = tmp.next