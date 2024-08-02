from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        This method calculates the minimum number of swaps required to group all 1's in a circular array.
        """
        
        zeros = 0            # Count of zeroes in the current window.
        n = len(nums)        
        minswaps = n + 1     # Initialize minswaps with a large value.
        window = nums.count(1) # Number of 1's in the array (window size).
        i = 0                # Start index of the window.
        j = 0                # End index of the window.
        
        # Initialize the zeroes count for the first window.
        for j in range(window):
            if nums[j] == 0:
                zeros += 1
        
        # Update minswaps for the initial window.
        minswaps = min(minswaps, zeros)

        # Slide the window across the circular array.
        while i < n:
            j = ((i + window) % n) - 1  # Calculate the new end index of the window. --> since it is a circular array

            # Increment zeroes count if the new element is 0.
            if nums[j + 1] == 0:
                zeros += 1

            # Decrement zeroes count if the outgoing element is 0.
            if nums[i] == 0:
                zeros -= 1

            i += 1
            j += 1

            # Update minswaps with the minimum zeroes count in the current window.
            minswaps = min(minswaps, zeros)

        return minswaps  # Return the minimum number of swaps required.

# Algorithm/Approach: Sliding Window with Circular Array Handling
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
