class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Helper function to remove pairs and calculate the score
        def removePairs(s, c1, c2, score):
            stack = []
            tmpScore = 0
            # Iterate through each character in the string
            for char in s:
                # If the top of the stack is c1 and the current character is c2, remove the pair
                if stack and stack[-1] == c1 and char == c2:
                    stack.pop()
                    tmpScore += score
                else:
                    stack.append(char)
            # Return the score for removed pairs and the remaining string
            return tmpScore, ''.join(stack)

        score = 0
        # Choose the order of removing pairs based on which pair has a higher score
        if x > y:
            # Remove 'ab' pairs first
            score1, s = removePairs(s, 'a', 'b', x)
            # Then remove 'ba' pairs
            score2, s = removePairs(s, 'b', 'a', y)
        else:
            # Remove 'ba' pairs first
            score1, s = removePairs(s, 'b', 'a', y)
            # Then remove 'ab' pairs
            score2, s = removePairs(s, 'a', 'b', x)
        
        # Return the total score
        return score1 + score2


# locate higher scored pair using top of stack and string, score, repeat for lower scored pair

# Time Complexity
# O(n)
# Space Complexity
# O(n)
# Algorithm Approach
# Greedy algorithm with a Stack-based approach.
