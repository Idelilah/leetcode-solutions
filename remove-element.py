class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        expectedNums=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
                expectedNums.append(nums[i])
        print(expectedNums)
        return k
