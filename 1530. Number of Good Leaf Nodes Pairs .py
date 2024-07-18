# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0  # Variable to store the count of good leaf node pairs
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  # If node is a leaf, return a list with distance 1

            left_dist = dfs(node.left)  # Recursive call on left subtree
            right_dist = dfs(node.right)  # Recursive call on right subtree

            # Check all pairs of leaf nodes from left and right subtrees
            for l in left_dist:
                for r in right_dist:
                    if l + r <= distance:
                        self.pairs += 1  # Increment pairs count if the sum of distances is less than or equal to the given distance

            dist = left_dist + right_dist
            return [d + 1 for d in dist]  # Increment distances of all leaf nodes in the current subtree by 1

        dfs(root)
        return self.pairs  # Return the count of good leaf node pairs

"""
Approach:
1. Perform a DFS traversal on the binary tree.
2. For each node, gather distances of leaf nodes from its left and right subtrees.
3. For each pair of leaf nodes (one from the left subtree and one from the right subtree), check if their combined distance is less than or equal to the given distance.
4. If so, increment the count of good leaf node pairs.
5. Return the total count of good leaf node pairs.

Time Complexity: O(n^3) in the worst case
Space Complexity: O(n)

"""
