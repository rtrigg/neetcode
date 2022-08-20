"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Diameter is the max of the 1) diameter of the left, 2) the diameter of the right,
    and 3) the height of the left plus the height of the right subtrees.
    """

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            self.maxDepth(root.left) + self.maxDepth(root.right),
        )

    def maxDepth(self, root: TreeNode, depth=0):
        if root is None:
            return depth
        depth += 1
        return max(self.maxDepth(root.left, depth), self.maxDepth(root.right, depth))
