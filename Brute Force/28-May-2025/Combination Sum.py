'''
Combination Sum
medium
Recursion, backtracking, array
'''

'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
'''

from typing import List

class Solution:
    '''
    IMPORTANT NOTE:
    for loop is used in recursion when either at every step all the options are available or all options from the current element are available including the current element
    
    For example in this question, at every step we have the array from the current element till end available so we use a for loop
    Only from current are available to avoid duplicate permutations
    But if duplicate permutations were allowed we would have taken full array at each step eliminating the need of a startIdx because we always start from 0
    
    But for questions where taking the same elment is not allowed then we only focus on next element and recurse on whether to take it or leave it
    In this case we do not need a for loop
    For example the subset generation question where we have to generate all subsets of a given array
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        1. Keep a result array to store all subsets
        2. Recurse from the current element till end to avoid duplicate permutations
        3. At each element, add it to currSum, push it in subset and call recursion on it
        4. If we have reached the target sum then add the current subset to result
        5. If not then continue with elements from current till end of array
        6. If at any point we exceed the target then reaching target is not possible
        '''
        
        def helper(startIdx, currSum, subset=[]):
            if currSum == target:
                print('GOT SUBSET:', subset)
                result.append(subset.copy())
                return
            
            if currSum > target:
                return
            
            for i in range(startIdx, len(candidates)):
                subset.append(candidates[i])
                helper(i, currSum+candidates[i], subset)
                subset.pop()
        
        result = []
        helper(0, 0)

        return result