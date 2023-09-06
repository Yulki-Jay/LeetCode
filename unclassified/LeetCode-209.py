class Solution:
    def minSubArrayLen1(self, target, nums) -> int: # 两层循环会超时
        min = len(nums) + 1 
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum >= target:
                    if j-i + 1 <= min:
                        min = j-i + 1
                    break # 开始下一个循环
        return 0 if min == len(nums) + 1 else min
    def minSubArrayLen(self, target, nums) -> int:
        slow = fast = 0
        sum = 0
        min_value = len(nums) + 1 # 目前判断没有窗口符合条件
        while slow <= len(nums)-1 and fast <= len(nums)-1:# 最多能移动到最后一个len - 1
            print('Hello')             
            while sum<= target and fast < len(nums): # fast最多能到len-1的位置
                sum += nums[fast]  # 最后一个元素也加上了 
                if sum< target:
                    fast += 1
            # fast窗口的位置找到了
            # 已经找到了，那么就要开始移动slow了
            tmp =  fast - slow + 1
            min_value = min(tmp,min_value)
            while sum >= target and slow < len(nums): # slow最多能到len-1的位置
                sum -= nums[slow]
                if sum>target:
                    slow += 1
            # slow的位置找到了
            fast += 1
        return 0 if min_value == len(nums) + 1 else min_value

        
  
        
target = 9
nums = [1,2,3,4,5]
solution = Solution()
print(solution.minSubArrayLen(target,nums))