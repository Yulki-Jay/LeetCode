class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 思路用栈进行实现就好了，如果是#就弹出呗
        flag = False
        s = list(s)
        t = list(t)
        stack_s = []
        stack_t = []
        for i in range(len(s)):
            if s[i] == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
        for j in range(len(t)):
            if t[j] == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t[j])
        return stack_s == stack_t
        
        
        
s = "#a#c"
t = "c"  
solution =Solution()    
print(solution.backspaceCompare(s,t))

