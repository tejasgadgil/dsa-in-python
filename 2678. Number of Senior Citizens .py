from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        This method counts the number of senior passengers (age > 60) based on the details provided.
        """
        senior = 0  # Initialize the count of senior passengers to zero.

        # Iterate through each passenger's details in the list.
        for psngr in details:
            # Extract the age from the substring and check if it's greater than 60.
            if int(psngr[11] + psngr[12]) > 60:
                senior += 1  # Increment the count of senior passengers.

        return senior  # Return the final count of senior passengers.

# Algorithm/Approach: Linear Scan
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
