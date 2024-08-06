from collections import Counter
from typing import List

class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        This method calculates the minimum number of pushes needed to type the word on a classic mobile keypad.
        """
        count = Counter(word)  # Count the frequency of each character in the word.
        # Sort the characters by their frequency in descending order.
        count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        n = len(count)  # Number of unique characters.
        press = 0  # Initialize the number of pushes.
        
        # Calculate the total number of pushes.
        for i in range(n):
            press += count[i][1] * ((i // 8) + 1) # after 8 buttons are used, back to first button, next position of char
        
        return press  # Return the total number of pushes.

# Algorithm/Approach: Frequency Counting and Sorting
#
# Time Complexity: O(m log m)
# - Counting the frequency of characters takes O(m) time, where m is the length of the word.
# - Sorting the characters by their frequency takes O(m log m) time.
# - Therefore, the overall time complexity is O(m log m).
#
# Space Complexity: O(m)

