import unittest

class TreeNode:
    def __init__(self, val: int = 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        return self._dfs(root, root.val)
    
    def _dfs(self, node: TreeNode, max_path_value: int) -> int:
        if not node:
            return 0
            
        # Determine if the current node is good
        is_good_node = 1 if node.val >= max_path_value else 0
        
        # Update the maximum value seen so far for child nodes
        updated_max_value = max(max_path_value, node.val)
        
        # Recursively count good nodes in left and right subtrees
        left_good_nodes = self._dfs(node.left, updated_max_value)
        right_good_nodes = self._dfs(node.right, updated_max_value)
        
        return is_good_node + left_good_nodes + right_good_nodes

# Unit tests for BinaryTreeGoodNodes
class TestBinaryTreeGoodNodes(unittest.TestCase):
    def setUp(self):
        """Set up the test cases."""
        self.solver = Solution()
    
    def test_example_case(self):
        """Test the example case: [3,1,4,3,null,1,5]."""
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        self.assertEqual(self.solver.goodNodes(root), 4)
    
    def test_single_node(self):
        """Test a tree with a single node."""
        root = TreeNode(1)
        self.assertEqual(self.solver.goodNodes(root), 1)
    
    def test_empty_tree(self):
        """Test an empty tree."""
        self.assertEqual(self.solver.goodNodes(None), 0)
    
    def test_skewed_tree(self):
        """Test a skewed tree (all nodes in one direction)."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solver.goodNodes(root), 3)
    
    def test_negative_values(self):
        """Test a tree with negative values."""
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-1)
        self.assertEqual(self.solver.goodNodes(root), 2)
    
    def test_duplicate_values(self):
        """Test a tree with duplicate values."""
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertEqual(self.solver.goodNodes(root), 3)

if __name__ == '__main__':
    unittest.main()