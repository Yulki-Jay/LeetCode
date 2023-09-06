# 26 进制
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        length = len(columnTitle)
        for i in range(0,length):
            res = res + (ord(columnTitle[i]) - ord('A') + 1) *26 **(length - i -1)
        return res
    

    
solution = Solution()
print(solution.titleToNumber('ZY'))


# B = 2
# CB = 3*26 + 2
# CBD = 3*26*26 + 2*26 + 4