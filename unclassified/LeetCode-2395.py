# 给你一个下标从 0 开始的整数数组 nums ，判断是否存在 两个 长度为 2 的子数组且它们的 和 相等。注意，这两个子数组起始位置的下标必须 不相同 。

# 如果这样的子数组存在，请返回 true，否则返回 false 。

# 子数组 是一个数组中一段连续非空的元素组成的序列。



class Solution:
    def findSubarrays(self, nums) -> bool:
        for i in range(len(nums)-1):
            res = 0
            res = nums[i] + nums[i+1]
            for j in range(i+1,len(nums)-1):
                if nums[j] + nums[j+1] == res:
                    return True
        return False

                    
            

solution = Solution()
print(solution.findSubarrays([0,0,0]))