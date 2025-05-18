# Start merging from end so that if all elemts of nums2 are largest then all 
# zeros in nums1 are replaced and if any from nums1 is bigger then the last in nums1
# can then be safely replaced with something from nums2

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for nums1 and nums2, and the final position in nums1
        p1 = m - 1  # Pointer for the last valid element in nums1
        p2 = n - 1  # Pointer for the last element in nums2
        p = m + n - 1  # Pointer for the last position in nums1
        
        # Merge nums1 and nums2 starting from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # Place the larger value at the end
                p1 -= 1  # Move pointer in nums1
            else:
                nums1[p] = nums2[p2]  # Place the larger value from nums2
                p2 -= 1  # Move pointer in nums2
            p -= 1  # Move final pointer
        
        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        