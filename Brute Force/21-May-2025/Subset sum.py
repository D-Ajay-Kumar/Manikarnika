'''
Subset sum
easy
recursion, dfs, array
'''

'''
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples:

Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8
'''

def subsetSum(nums):
    '''
    1. At each index we can either choose to pick the number or not
    2. If say, picking the number is left child and not picking the right child
    3. Then for subset with all elements we can go all left at every recursive call
    4. For empty subset we can go all right at every recursion call
    5. If we want to select one element, then right till the element, left on it and then right again till the end
    6. Once index goes out of the array, we have finished a combination
    7. Add the subset sum to ans array and return from there
    '''
    def subsetSumHelper(idx, currSum):
        # If index runs out then append and return
        if idx == n:
            ans.append(currSum)
            return
        
        # The left recursive call to include the number
        subsetSumHelper(idx+1, currSum+nums[idx])
        # The right recursive call to exclude the number
        subsetSumHelper(idx+1, currSum)
            
    
    n = len(nums)
    ans = []
    subsetSumHelper(0, 0)
    
    return ans


if __name__ == '__main__':
    ans = [0, 1, 2, 3, 5, 6, 7, 8]
    print(ans == sorted(subsetSum([5, 2, 1])))