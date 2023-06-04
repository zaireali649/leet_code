from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m+n-1, -1, -1):
            if n > 0 and m > 0:
                if nums2[n-1] >= nums1[m-1]:
                    nums1[i] = nums2[n-1]
                    n = n - 1
                else:
                    nums1[i] = nums1[m-1]
                    m = m - 1
            elif n > 0:
                nums1[i] = nums2[n-1]
                n = n - 1
            else:
                nums1[i] = nums1[m-1]
                m = m - 1