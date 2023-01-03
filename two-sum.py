class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == 0:
                    if nums[i] == 0 and nums[j] == 0:
                        return i, j
                if nums[i] + nums[j] == target:
                    return i, j