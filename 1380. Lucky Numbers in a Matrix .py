from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []  # List to store lucky numbers
        maxCol = set()  # Set to store the maximum elements of each column

        # Step 1: Find the maximum elements in each column and add them to maxCol
        for j in range(len(matrix[0])):
            maxi = matrix[0][j]
            for i in range(len(matrix)):
                maxi = max(matrix[i][j], maxi)
            maxCol.add(maxi)

        # Step 2: Check each row to find if the minimum element is in maxCol
        for row in matrix:
            if min(row) in maxCol:
                res.append(min(row))

        return res

"""
Approach:
1. Find the maximum elements in each column and store them in a set.
2. For each row, find the minimum element and check if it exists in the set of column maximums.
3. If it does, add it to the result list.

Time Complexity:
- O(m * n) where m is the number of rows and n is the number of columns.

Space Complexity:
- O(max(m, n)) for storing the result list and the set of column maximums.
"""
