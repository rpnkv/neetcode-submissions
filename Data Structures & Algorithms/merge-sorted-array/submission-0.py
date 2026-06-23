class Solution:
    def merge(self, nums1: List[int],
              m: int,
              nums2: List[int],
              n: int
              ) -> None:
        
        m,n = m - 1, n - 1
        vacant = len(nums1) - 1

        while m >= 0 and n >=0:
            if nums1[m] > nums2[n]:
                nums1[vacant] = nums1[m]
                m-= 1
            else:
                nums1[vacant] = nums2[n]
                n -= 1

            vacant -= 1
        
        if n >=0:
            nums1[:n + 1] = nums2[:n+1]
