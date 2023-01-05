class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ln=n+m
        pt=0
        while ln>m:
            nums1[m]=nums2[pt]
            pt+=1
            m+=1
        nums1.sort()
        print(nums1)