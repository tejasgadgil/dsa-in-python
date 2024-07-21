class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        # Initialize the starting player to 0 (Bob)
        start = 0
        
        # Loop until either x or y becomes negative
        while x >= 0 and y >= 0:
            # Increment the player turn counter
            start += 1
            # Decrement x by 1 and y by 4
            x -= 1
            y -= 4

        # Determine the losing player based on the number of turns
        if start == 0:
            return "Bob"
        elif start % 2 == 0:
            return "Alice"
        else:
            return "Bob"

"""
Time Complexity:
- The loop runs until either x or y becomes negative.
- In the worst case, it runs O(min(x, y/4)) times.
- Therefore, the time complexity is O(min(x, y/4)).

Space Complexity:
- The algorithm uses a constant amount of space.
- Therefore, the space complexity is O(1).
"""
