'''
Count good nodes in a binary tree
medium
binary_tree, dfs, preorder
'''

'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''

import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        1. We do a DFS preorder on the tree and keep track of the largest seen so far
        2. If the value of current node is greater than or equal to largest so far then we increase good nodes count and update largest to current node's value
        3. Then we do DFS on left and pass to it the largest so far
        4. Then we do DFS on right and pass to it the largest so far
        5. Why we are not keeping largest outside DFS like good nodes count? Because largest needs to be reset when we go from left branch of a node to the right branch
        '''

        # DFS helper method which takes node and largest on that route so far
        def preorderDfs(node, largestSoFar):
            # If we have reached a null node then return
            if not node:
                return
            
            # Check if current node is greater than largest we have seen so far
            if node.val >= largestSoFar:
                nonlocal goodNodesCount
                # Increase good nodes count
                goodNodesCount += 1
                # Update largest so far
                largestSoFar = node.val
            
            # Iterate over the rest of the child nodes
            preorderDfs(node.left, largestSoFar)
            preorderDfs(node.right, largestSoFar)

        
        # Good nodes count can stay outside as it doesn't reset throughout traversal
        goodNodesCount = 0
        preorderDfs(root, -math.inf)

        return goodNodesCount