'''
Search in rotated sorted array
medium
modified binary search, array
'''

'''
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.
'''

from typing import List

class Solution:
    '''
    1. Draw the graph for the rotated sorted array and observe the two parts by arbitrarily assuming middle on one of the two parts
    2. Check how the relationship between left and mid value helps determine which part is sorted
    3. If left is bigger than mid then definitely right part is sorted, left may or may not be
    4. If left is smaller than mid then definitely left part is sorted, right may or may not be
    5. Whichever part is sorted, check if target is in that range according to which adjust left or right pointer
    6. Return the mid if we match target otherwise -1 at the end of the loop
    '''
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Edge case where there is only one element
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            
            # If left is strictly larger than mid then we are surely in right part and all elements right to mid are sorted for sure
            if nums[left] > nums[mid]:
                # Check if target is in the right part of the array as it is definitely sorted
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                    continue
                else:
                    right = mid-1
                    continue
            # If not, then we are in left part and all elementes to left must be sorted
            else:
                # Check if target is in the left part which is definitely sorted
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                    continue
                else:
                    left = mid+1
                    continue

        return -1
            

