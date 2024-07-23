from collections import defaultdict
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        def customSort(n):
            return (numHash[n], -n)

        # Create a frequency dictionary to count occurrences of each number
        numHash = defaultdict(int)
        for num in nums:
            numHash[num] += 1
        
        # Sort the list based on the custom sorting key
        nums.sort(key=customSort)
        return nums
# Approach:
# Comparator
# Time Complexity:
# O(nlogn).
# Space Complexity:
# O(n).
