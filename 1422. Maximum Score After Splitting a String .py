class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize the count of '0's on the left (l) based on the first character
        l = 1 if s[0] == '0' else 0

        # Initialize the count of '1's on the right (r)
        # If the first character is '0', count all '1's in the string for the right
        # Otherwise, exclude the first character in the count
        r = s.count('1') if l == 1 else (s.count('1') - 1)

        # Initialize max_score with the sum of '0's on the left and '1's on the right
        max_score = l + r

        n = len(s)  # Length of the string

        # Iterate through the string (excluding the last character) to update scores
        for i in range(1, n - 1):
            if s[i] == '1':
                r -= 1  # A '1' moves from the right to the left partition
            else:
                l += 1  # A '0' moves from the right to the left partition

            # Update max_score to the maximum score found so far
            max_score = max(max_score, l + r)

        # Return the maximum score found
        return max_score

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Iterative Partitioning Scoring
