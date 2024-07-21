from collections import defaultdict
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def dfs(src, adj, visit, path, order):
            # Detect cycle: return False if current node is already in the current path
            if src in path:
                return False
            # Return True if current node is already visited
            if src in visit:
                return True

            visit.add(src)
            path.add(src)

            # Perform DFS on all neighbors
            for neigh in adj[src]:
                if not dfs(neigh, adj, visit, path, order):
                    return False

            # Remove current node from the path and add to the order
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adj = defaultdict(list)
            # Build adjacency list
            for src, dst in edges:
                adj[src].append(dst)
            
            visit, path = set(), set()
            order = []

            # Perform DFS for all nodes
            for src in range(1, k+1):
                if not dfs(src, adj, visit, path, order):
                    return []

            # Return topological sort in correct order
            return order[::-1]

        # Get topological order for row and column conditions
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        # Map values to their respective row and column indices
        val_to_row = {n:i for i, n in enumerate(row_order)}
        val_to_col = {n:i for i, n in enumerate(col_order)}

        # Check for cycle detection
        if not row_order or not col_order:
            return []

        # Initialize the matrix
        matrix = [[0]*k for _ in range(k)]

        # Fill the matrix according to the row and column orders
        for num in range(1, k+1):
            r, c = val_to_row[num], val_to_col[num]
            matrix[r][c] = num

        return matrix

    """
    Approach:
    1. Perform topological sort on rowConditions to get the order of rows.
    2. Perform topological sort on colConditions to get the order of columns.
    3. Map the values to their respective positions in the matrix.
    4. Detect cycles using DFS during topological sorting. If a cycle is detected, return an empty matrix.

    Time Complexity:
    - Topological Sort: O(k + E), where k is the number of nodes and E is the number of edges.
    - Filling the matrix: O(k).
    - Overall: O(k + E).

    Space Complexity:
    - Adjacency list: O(k + E).
    - Visit, path sets: O(k).
    - Order list: O(k).
    - Matrix: O(k^2).
    """
