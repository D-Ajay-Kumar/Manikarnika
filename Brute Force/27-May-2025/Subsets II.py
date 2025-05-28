'''
Subsets II
medium
Recursion, string, backtracking
'''

'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''

from typing import List

class Solution:
    '''
    1. Sort nums in the very beginning because (1, 2) is considered different from (2, 1)
    2. Recursively pick and not pick each element
    3. If we reach end of nums then add the resultant subset to the set as a tuple because lists are not hashable
    4. Convert the set to a list at the end to return
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, subset=[]):
            # If at end of array
            if idx == len(nums):
                # Add subset to set as a tuple
                resultSet.add(tuple(subset))
                return
            
            # Include the current number and recurse
            subset.append(nums[idx])
            helper(idx+1, subset)

            # Exclude the current number and recurse
            subset.pop()
            helper(idx+1, subset)

        resultSet = set()
        nums.sort()
        helper(0)

        # Convert the set of tuples to a list of lists
        resultList = list(resultSet)
        return resultList
    
sol = Solution()
a = sol.subsetsWithDup([1, 2, 2])
print(a)