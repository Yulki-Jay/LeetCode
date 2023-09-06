class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])
    

s = "   fly me   to   the moon  "  
solution = Solution()
print(solution.lengthOfLastWord(s))