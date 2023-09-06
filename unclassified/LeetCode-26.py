class Solution:
    def removeDuplicates(self, nums):
        res = 0
        slow_pointer = 0
        fast_pointer = 1
        length = len(nums)
        while fast_pointer < length:
            # slow 和 fast 一个一个移动
            while fast_pointer < length and  nums[fast_pointer] == nums[slow_pointer]:
                fast_pointer += 1
            if fast_pointer < length: 
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]
                fast_pointer += 1

        return slow_pointer+1, nums


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5]
nums2 = [1,1,2]
print(s.removeDuplicates(nums2))
