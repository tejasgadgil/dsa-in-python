# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Helper function to perform DFS and find the path to a target node
        def dfs(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return path
            
            # Traverse left
            path.append("L")
            res = dfs(node.left, path, target)
            if res:
                return res
            path.pop()  # Backtrack

            # Traverse right
            path.append("R")
            res = dfs(node.right, path, target)
            if res:
                return res
            path.pop()  # Backtrack

            return ""

        # Find the path to the startValue node
        start_path = dfs(root, [], startValue)
        # Find the path to the destValue node
        dest_path = dfs(root, [], destValue)

        # Find the common prefix length
        i = 0
        while i < min(len(start_path), len(dest_path)) and start_path[i] == dest_path[i]:
            i += 1

        # Remove the common prefix and replace start path with 'U'
        return "".join(["U"] * len(start_path[i:]) + dest_path[i:])

# Time Complexity: O(n)
# Space Complexity: O(h + n)

# Time Complexity:
# The DFS traversal takes O(n) time, where n is the number of nodes in the tree, since in the worst case, the DFS will visit every node.
# Constructing paths and finding the common prefix takes O(L) time, where L is the length of the paths.
# The overall time complexity is O(n+L), which simplifies to O(n) since L is at most n.
# Space Complexity:
# The space complexity is O(h), where h is the height of the tree. 
# This is due to the recursive call stack in the DFS traversal.
# Additional space for storing paths is O(L), but since L≤n, the overall space complexity is O(h+n).

# Approach:
# 1. Use DFS to find paths from the root to the start and destination nodes.
# 2. Compare the paths to find the common ancestor.
# 3. Replace the path from start to common ancestor with 'U' and append the path from the common ancestor to the destination.
