from collections import defaultdict
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        This method finds the k-th distinct string in the array.
        """
        firstOcc = defaultdict(int)  # Dictionary to store the occurrence count of each string.
        n = len(arr)  # Length of the array.
        
        # Count the occurrences of each string in the array.
        for i in range(n):
            firstOcc[arr[i]] += 1

        distinct = []  # List to store distinct strings.
        
        # Collect strings that occur exactly once.
        for i in range(n):
            if firstOcc[arr[i]] == 1:
                distinct.append(arr[i])

        # Check if there are at least k distinct strings.
        if len(distinct) < k:
            return ""

        return distinct[k-1]  # Return the k-th distinct string.

# Algorithm/Approach: HashMap and List
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)
