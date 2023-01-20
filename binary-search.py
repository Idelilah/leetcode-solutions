class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            ptr= (l+r)//2
            if nums[ptr]<target:
                l=ptr+1
            elif nums[ptr]>target:
                r=ptr-1
            else:
                return ptr
        return -1

