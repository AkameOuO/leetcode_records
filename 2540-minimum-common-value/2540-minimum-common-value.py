class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.reverse()
        nums2.reverse()
        while nums1 and nums2:
            if nums1[-1] == nums2[-1]:
                return nums1[-1]
            
            if nums1[-1] < nums2[-1]:
                nums1.pop()
            else:
                nums2.pop()
        return -1