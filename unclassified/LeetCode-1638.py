# 我的思路是先把所有的子字符串全部保存到hash表当中去
# 然后依次比较每个key
# key中只能有一个元素不同，如果超过一个就不是答案了

from collections import defaultdict # 我的这个方法太蠢了
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        # 首先将字符转换为字典
        s_dic = defaultdict(int) 
        t_dic = defaultdict(int)
        s_length = len(s) # 3
        t_length = len(t) # 4
        for i in range(1,s_length+1): # 【1,3】
            for j in range(0,s_length-i+1): # 保证把最后一个元素加入里面,这地方有问题 
                s_dic[s[j:j+i]] = s_dic[s[j:j+i]] + 1 
        for i in range(1,t_length+1):
            for j in range(0,t_length-i+1): # 保证把最后一个元素加入里面 
                t_dic[t[j:j+i]] = t_dic[t[j:j+i]] + 1 
        for key_s in s_dic.keys():
            for key_t in t_dic.keys():
                if len(key_s) != len(key_t):
                    continue
                else:
                    diff = 0 # 用来判断有哪两个字符不相同的
                    for ii in range(len(key_s)):
                        if key_s[ii] != key_t[ii]:
                            diff += 1   
                    if diff == 1:
                        res += s_dic[key_s] * t_dic[key_t]
                    else:
                        continue
                    
        return res
 
 
 
s = "abe"
t = "bbc"
solution = Solution()
print(solution.countSubstrings(s,t))

