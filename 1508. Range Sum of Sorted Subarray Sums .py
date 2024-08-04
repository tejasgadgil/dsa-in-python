from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, l: int, r: int) -> int:
        """
        This method calculates the sum of subarray sums within a specified range.
        """
        result = []  # List to store all subarray sums.

        # Calculate all subarray sums and store them in the result list.
        for i in range(n):
            tempSum = 0
            for j in range(i, n):
                tempSum += nums[j]
                result.append(tempSum)

        result.sort()  # Sort the subarray sums.
        total_sum = 0  # Initialize the total sum.
        mod = int(1e9) + 7  # Modulo value to prevent overflow.

        # Calculate the sum of the subarray sums within the range [l, r].
        for i in range(l - 1, r):
            total_sum = (total_sum + result[i]) % mod

        return total_sum  # Return the final sum.

# Algorithm/Approach: Brute Force and Sorting
#
# Time Complexity: O(n^2 log n)
# - Calculating all subarray sums takes O(n^2) time.
# - Sorting the subarray sums takes O(k log k) time, where k is the number of subarray sums, which is n(n + 1) / 2.
# - Since k = O(n^2), the sorting step takes O(n^2 log n^2) = O(n^2 log n) time.
# - Therefore, the overall time complexity is O(n^2 log n).
#
# Space Complexity: O(n^2)
# - The space complexity is O(k), where k is the number of subarray sums, which is n(n + 1) / 2.
# - This is due to storing all subarray sums in the result list.
