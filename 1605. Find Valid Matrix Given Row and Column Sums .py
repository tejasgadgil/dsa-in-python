class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the resulting matrix with zeros
        matrix = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]

        # Fill the matrix
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                # Get the minimum of rowSum[i] and colSum[j]
                minm = min(rowSum[i], colSum[j])
                # Assign the minimum value to the matrix cell
                matrix[i][j] = minm
                # Subtract the assigned value from rowSum and colSum
                rowSum[i] -= minm
                colSum[j] -= minm

        return matrix

    """
    Approach: Greedy Approach
    1. Iterate through each cell of the matrix.
    2. For each cell, assign the minimum value between the remaining row sum and column sum.
    3. Deduct the assigned value from both the row sum and column sum.
    4. Continue until all cells are filled.

    Time Complexity:
    - O(m * n) where m is the number of rows and n is the number of columns.

    Space Complexity:
    - O(m * n) for the resulting matrix.
    """
