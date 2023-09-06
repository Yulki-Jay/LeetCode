class Solution:
    def removeElement(self, nums, val) : # 最后的返回值是数组的新长度
        res = 0
        length = len(nums)
        first = len(nums)
        i = 0
        while i < length:
            if nums[i]==val:
                res += 1
                for j in range(i,length-1):
                    nums[j]=nums[j+1]
                length -= 1
            if nums[i]!=val:
                i += 1
        return length,nums
            
        
                

nums = [0,1,2,2,3,0,4,2]
val = 2 
s = Solution()
print(s.removeElement(nums,val))
    
    
