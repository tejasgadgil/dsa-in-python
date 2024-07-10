class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Initialize a counter to keep track of how far we are from the main folder
        away = 0

        # Iterate through each log entry
        for log in logs:
            # If the log entry is "../" and we are not already at the main folder
            if log == "../" and away > 0:
                # Move one folder up (closer to the main folder)
                away -= 1
            # If the log entry is "../" but we are at the main folder or the log entry is "./"
            elif (log == "../" and away == 0) or log == "./":
                # Do nothing, continue to the next log entry
                continue
            # Otherwise, the log entry represents moving into a subdirectory
            else:
                # Move one folder deeper (further from the main folder)
                away += 1

        # Return the number of steps away from the main folder
        return away

# Time Complexity
# O(n)
# Space Complexity
# O(1)
# Algorithm Approach
# Greedy 
