# 判断前面的串是否可以由后面的串进行创建
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = [0] * 26 
        for ch in magazine:
            res[ord(ch) - ord('a')] +=1
        for ch in ransomNote:
            res[ord(ch) - ord('a')] -=1
        for i in range(26):
            if res[i] < 0:
                return False
        return True
    
    
    
ransomNote = "aa"
magazine = "ab"
s = Solution()
print(s.canConstruct(ransomNote=ransomNote,magazine=magazine))