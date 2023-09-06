# 二叉树的中序遍历算法
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
result = []
class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        def inorder(self,root:TreeNode):
           # 左中右
           if root == None:
              return
           inorder(self,root.left)
           result.append(root.val)
           inorder(self,root.right)
        inorder(self,root)
        return result

root = [1,None,2,3]    
    
#s = Solution()
#print(s.inorderTraversal([1,None,2,3]))

a = [1,2,3]
print(a[::-1])

# 如果不用递归的情况下，就需要用到栈的操作了
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root == None:
#             return []
#         stack = [] # 用来当做栈
#         res = []
#         p = root
#         while(p or stack[0]==None): # 如果p指向None或者栈为None
#             if(p): # 如果P不等于None
#                 stack.append(p)
#                 p = p.left # 找到最左下的节点
#             else:
#                 res.append(stack.pop)
#                 p = p.right
                
#         return res
                
        
        