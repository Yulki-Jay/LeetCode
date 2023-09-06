# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

#  

# 示例 1：

# 输入：nums = [3,2,3]
# 输出：3
from collections import defaultdict
class Solution:
    def majorityElement(self, nums) -> int:
        res = []
        length = len(nums)
        number = defaultdict(int)
        for num in nums:
            number[str(num)] = max(0,number[str(num)]) + 1
        # 已经获取到字典了
        for key in number.keys():
            if number[key] > length/2:
                res.append(key)
        return int(res[0])
    
solution = Solution()
print(solution.majorityElement([3,2,3]))
