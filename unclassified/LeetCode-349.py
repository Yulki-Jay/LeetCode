class Solution:
    def intersection1(self, nums1, nums2):
        return list(set(nums1) & set(nums2)) # 猴一下，一条代码
    def intersection(self, nums1, nums2):
        # 用字典弄吧，要不太刺激啦
        from collections import defaultdict
        source = defaultdict(int)
        target = defaultdict(int)
        res = []
        for i in nums1: # 用字典进行实现
            source[f'{i}'] += 1
        for i in nums2:
            target[f'{i}'] += 1
        for i in target.keys():
            if i in source.keys():
                res.append(int(i))
        return res
        
        



s =  Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersection(nums1,nums2))
    