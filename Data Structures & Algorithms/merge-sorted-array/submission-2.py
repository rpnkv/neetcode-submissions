class Solution:
    def merge(self, nums1: List[int],
              m: int,
              nums2: List[int],
              n: int
              ) -> None:
        i1, i2, vacant = m - 1, n - 1, len(nums1) - 1

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[vacant] = nums1[i1]
                i1 -= 1
            else:
                nums1[vacant] = nums2[i2]
                i2 -= 1
            
            vacant -= 1
        
        if i2 >=0:
            nums1[:i2 + 1] = nums2[:i2+1]
