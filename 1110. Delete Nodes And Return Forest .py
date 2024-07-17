# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_del: List[int]) -> List[TreeNode]:
        to_del = set(to_del)  # Convert list of nodes to delete into a set for O(1) lookups
        roots = set([root])   # Initialize a set with the root node

        def dfs(node):
            if not node:
                return None
            res = node
            if node.val in to_del:
                res = None
                roots.discard(node)  # Remove the current node from the set of roots
                if node.left:
                    roots.add(node.left)  # Add left child to the set of roots if it exists
                if node.right:
                    roots.add(node.right)  # Add right child to the set of roots if it exists
            node.left = dfs(node.left)  # Recursively delete nodes in the left subtree
            node.right = dfs(node.right)  # Recursively delete nodes in the right subtree
            return res

        dfs(root)  # Perform DFS starting from the root
        return list(roots)  # Convert the set of roots to a list and return it

'''
Approach:
1. Convert the list of nodes to be deleted into a set for faster lookups.
2. Initialize a set with the root node to keep track of potential roots of the resulting forest.
3. Use DFS to traverse the tree and delete nodes:
   - If a node is in the set of nodes to be deleted, set its value to None.
   - If a node is deleted, remove it from the set of roots and add its non-null children to the set of roots.
   - Recursively process the left and right children.
4. Return the set of roots converted to a list.

Time Complexity: O(n)
- The algorithm visits each node exactly once, where n is the number of nodes in the tree.

Space Complexity: O(n)
- The space complexity is O(n) due to the additional space used for the set of roots, the set of nodes to be deleted, and the recursive call stack.
'''
