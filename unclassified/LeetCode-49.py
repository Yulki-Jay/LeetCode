# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
# 这题有一点烦，如果不考虑时间复杂度和空间复杂度的话很容易,时间复杂度就是n * n 了，
# 先把所有数组先求出来，然后判断是否相同，如果相同的话，就把他添加到列表中就好了
# 可以最后保存的是位置
# 我需要保存的是什么

class Solution:
    def groupAnagrams(self, strs) :
        if not strs:
            return None # 没有字符串，直接返回空
        from collections import defaultdict
        res = defaultdict(list)
        for str in strs:
            res[''.join(sorted(str))].append(str)
        return [a for a in res.values()]
    def groupAnagrams1(self, strs) : # 这个版本我就用字典，我不用别的
        if not strs:
            return None # 没有字符串，直接返回空
        res = dict()
        for str in strs:
            key = ''.join(sorted(str))
            if key in res.keys():
                res[key].append(str)
            else:
                res[key]=[str]
        return [a for a in res.values()]
        
            
        
        
        

    
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"] # [["bat"],["nat","tan"],["ate","eat","tea"]]
s = Solution()
print(s.groupAnagrams1(strs=strs))

