class Solution:
    def isHappy(self, n: int) -> bool:
        from collections import defaultdict
        res = defaultdict(int)
        s = str(n)
        # 统计每个数字的平方吧
        while True:
            square = 0
            for i in range(len(s)):
                square += int(s[i]) **2
            # print(square)
            s = str(square)
            if square == 1:
                return True
            if square in res.keys():
                return False
            else: 
                res[square] += 1
            
        
s = Solution()
print(s.isHappy(2))
              