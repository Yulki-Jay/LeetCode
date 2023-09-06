# 给你一个字符串 s，找到 s 中最长的回文子串。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

#  

# 示例 1：

# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符



class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = 0
        longest_str = s[0]
        for l in range(2,length+1): # 窗口从1开始判断 1--length
            for j in range(0,length-l+1):
                if s[j:j+l]==s[j:j+l][::-1]:
                    if longest < l:
                        longest = l
                        longest_str = s[j:j+l]
                        break
        return longest_str
s = Solution()
str1 = 'aaaaa'
# print(str1[0:5][::-1])
print(s.longestPalindrome(str1))