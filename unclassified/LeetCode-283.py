class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 最简单的方法，两个循环
        for i in range(len(nums)):
            if nums[i]==0:
                flag = False
                for j in range(i,len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        flag =True
                        break
                if  not flag:
                    break     
        return nums
        
nums = [0]
s = Solution()
print(s.moveZeroes(nums))