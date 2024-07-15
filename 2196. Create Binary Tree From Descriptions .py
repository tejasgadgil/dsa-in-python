# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}  # Dictionary to store nodes by their values
        children = set()  # Set to track child nodes

        # Iterate through the descriptions to create nodes and build the tree
        for parent, child, isLeft in descriptions:
            # Create parent node if it does not exist
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            # Create child node if it does not exist
            if child not in nodes:
                nodes[child] = TreeNode(child)

            # Set the left or right child based on the description
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            # Add the child node to the set of children
            children.add(child)
        
        # Find the root node (a node that is not a child of any other node)
        for p, c, l in descriptions:
            if p not in children:
                return nodes[p]

        # Fallback in case the root node is not found
        return nodes[descriptions[0][0]]

'''
Time Complexity: O(n)
Space Complexity: O(n)
Approach: Binary Tree Construction
'''
