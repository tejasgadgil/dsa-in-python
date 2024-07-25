from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        
        # For each number in nums, create a tuple (mapped_number, original_index)
        for i, n in enumerate(nums):
            n = str(n)  # Convert the number to a string to iterate over each digit
            buildNumber = 0
            
            # Construct the mapped number based on the provided mapping
            for c in n:
                buildNumber *= 10
                buildNumber += mapping[int(c)]
                
            # Append the mapped number and its original index to the pairs list
            pairs.append((buildNumber, i))
        
        # Sort the pairs based on the mapped numbers (and by the original index in case of ties)
        pairs.sort()

        # Reconstruct the sorted nums array using the original indices
        return [nums[p[1]] for p in pairs]


# Approach
# Mapping Creation, sorting ,result reconstruction
# Time Complexity
# O(n⋅d+nlogn) often simplifies to O(nlogn)
# Space Complexity
# O(n)
