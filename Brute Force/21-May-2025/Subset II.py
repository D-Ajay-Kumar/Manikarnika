'''
Subset II
medium
recursion, dfs, array
'''

'''
Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.

Examples:

Example 1:

Input: array[] = [1,2,2]

Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
'''

def subset2(nums):
    '''
    1. Check explanation in Subset sum.py
    '''
    def subsetHelper2(idx, subset = []):
        if idx == n:
            # Sort depending on whether (1, 2) is considered same as (2, 1)
            subset.sort()
            # Lists are not hashable so convert to tuple first
            ans.add(tuple(subset))
            return
        
        # Cannot directly do subset.append inside the method as append doesn't return the array back
        subset.append(nums[idx])
        subsetHelper2(idx+1, subset)
        
        # Pop the above appended element for not-selected subtree
        subset.pop()
        subsetHelper2(idx+1, subset)
    
    n = len(nums)
    ans = set()
    nums.sort() # WHY??
    subsetHelper2(0)
    
    # Convert set of tuples of list of lists
    result = []
    for tup in ans:
        result.append(list(tup))
    
    return result


if __name__ == '__main__':
    ans = subset2([1, 2, 2])
    print(ans)
    
    