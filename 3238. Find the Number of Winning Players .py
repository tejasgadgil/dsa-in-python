from collections import defaultdict, Counter
from typing import List

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        """
        This method calculates the number of players who have more than i picks of the same item,
        where i is the player's index.
        """
        player = defaultdict(list)  # Dictionary to store picks for each player.

        # Populate the player dictionary with picks.
        for p in pick:
            player[p[0]].append(p[1])

        winner = 0  # Initialize the count of winning players.

        # Iterate over each player.
        for i in range(n):
            if i in player:
                counts = Counter(player[i])  # Count the occurrences of each item picked by the player.
                # Check if any item is picked more than i times.
                if any(count > i for count in counts.values()):
                    winner += 1  # Increment the count of winning players.

        return winner  # Return the total number of winning players.

# Algorithm/Approach: Dictionary and Counter
#
# Time Complexity: O(m + n)
# - Building the player dictionary takes O(m), where m is the number of picks.
# - Counting the occurrences of items for each player and checking the condition takes O(n).
# - Therefore, the overall time complexity is O(m + n).
#
# Space Complexity: O(m)
# - The space complexity is O(m) due to the player dictionary storing all picks.
