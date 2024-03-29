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
    Calculate the diameter and depth from the bottom up. The depth of the
    parent node is one plus the max depth of the two child nodes. The diameter
    is the depth of the left child plus the right, plus two.
    """

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        diameter = 0

        def depth_first_search(root):
            nonlocal diameter
            if root is None:
                return -1
            left_depth = depth_first_search(root.left)
            right_depth = depth_first_search(root.right)
            diameter = max(diameter, 2 + left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        depth_first_search(root)
        return diameter
