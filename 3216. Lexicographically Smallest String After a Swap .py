class Solution:
    def getSmallestString(self, s: str) -> str:
        # Convert the input string into a list of characters for easier manipulation
        s = list(s)
        
        # Traverse the string up to the second-to-last character
        for i in range(len(s) - 1):
            # Check if the current character and the next character have the same parity (both even or both odd)
            if int(s[i]) % 2 == int(s[i + 1]) % 2 and int(s[i + 1]) < int(s[i]):
                # Swap the characters if the current character is greater than the next character
                s[i], s[i + 1] = s[i + 1], s[i]
                
                # Return the modified string immediately after performing the swap
                return ''.join(s)
        
        # Return the original string if no swap was performed
        return ''.join(s)


# Time Complexity
# O(N)
# Space Complexity
# O(n).
# Algorithm Approach
# Greedy approach
