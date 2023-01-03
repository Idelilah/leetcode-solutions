class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=[]
        sum.append(nums[0])
        for i in range(len(nums)-1):
           sum.append(sum[i]+nums[i+1])
        return sum