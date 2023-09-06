class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # 每组成一个z字行的上半部分就需要2*numRows-2个字符，下半部分需要2*numRows-2个字符
        length = len(s) # 统计字符串长度
        res = {} # 保存结果
        for i in range(0,numRows):
            res[i]=[]
        div = length // (2*numRows-2) # 统计有多少个z字行 
        mod = length % (2*numRows-2) # 统计最后一个z字行的长度
        for i in range(0,div):# 生成每一行的字符串
            for row in range(0,numRows): # 共计有这么多z
                if row == 0: # 第一行
                    res[row].append(s[row+i*(2*numRows-2)])
                elif row == numRows-1: # 最后一行
                    res[row].append(s[row+i*(2*numRows-2)])
                else: # 其余每一行
                    res[row].append(s[row+i*(2*numRows-2)])
                    res[row].append(s[(2*(numRows-1)-row+i*(2*numRows-2))])
        # 最后一定是少于2*numRows-2的
        for i in range(0,mod):
            start = div*(2*numRows-2)
            if i<numRows:
                res[i % numRows].append(s[start+i])
            else:
                res[numRows-(i % numRows)-2].append(s[start+i])
        result = []
        for key in res.keys():
            tmp = ''
            tmp = tmp.join(res[key])
            result.append(tmp)
        return ''.join(result)
solution = Solution()
print(solution.convert('PAYPALISHIRING',4))
