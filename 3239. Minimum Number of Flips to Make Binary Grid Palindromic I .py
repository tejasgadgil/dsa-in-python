from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        """
        This method calculates the minimum number of flips required to make a grid symmetric 
        either by rows or by columns.
        """
        n = len(grid)         # Number of rows in the grid.
        rowlen = len(grid[0]) # Number of columns in the grid.
        
        # Calculate the number of swaps needed to make rows symmetric.
        rowswaps = 0
        for row in grid:
            for i in range(rowlen // 2):
                if row[i] != row[rowlen - i - 1]:
                    rowswaps += 1

        # Calculate the number of swaps needed to make columns symmetric.
        colswaps = 0
        for i in range(rowlen):
            for j in range(n // 2):
                if grid[j][i] != grid[n - j - 1][i]:
                    colswaps += 1

        # Return the minimum number of swaps required.
        return min(colswaps, rowswaps)

# Algorithm/Approach: Symmetry Check with Two-Pointer Technique
#
# Time Complexity: O(n * m)
#
# Space Complexity: O(1)
