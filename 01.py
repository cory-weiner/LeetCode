from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            if target-v in nums and i != nums.index(target-v):
                return [i, nums.index(target-v)]
        
solution = Solution()
print(solution.twoSum([3,2,4],6))

