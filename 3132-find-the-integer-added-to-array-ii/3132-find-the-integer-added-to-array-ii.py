class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.sort()
        t2 = nums2[0]
        l2 = list(map(lambda x:x-t2,nums2))
        c2 = Counter(l2)
        nums1.sort()
        for i in range(2,-1,-1): #range(3):
            t1 = nums1[i]
            l1 = list(map(lambda x:x-t1,nums1))
            c1 = Counter(l1)
            c3 = c1 - c2
            print(c3)
            if sum(c3.values()) == 2:
                return t2 - t1
        return 0