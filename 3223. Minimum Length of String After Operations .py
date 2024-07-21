class Solution:
    def minimumLength(self, s: str) -> int:
        # If the string has less than 3 characters, return its length
        if len(s) < 3:
            return len(s) 

        # Dictionary to count occurrences of each character
        letters = {}
        
        # Iterate through each character in the string
        for i in s:
            # If the character is already in the dictionary
            if i in letters:
                # Increment its count
                letters[i] += 1
                # If its count reaches 3, reset it to 1
                if letters[i] == 3:
                    letters[i] = 1
            else:
                # If the character is not in the dictionary, add it with count 1
                letters[i] = 1
        
        # Initialize a count variable to sum up the final counts
        count = 0
        
        # Sum up the counts of each character
        for l in letters:
            count += letters[l]

        return count

"""
Approach:
1. If the length of the string is less than 3, return its length.
2. Use a dictionary to count occurrences of each character in the string.
3. If a character's count reaches 3, reset it to 1.
4. Sum up the counts of each character and return the sum.

Time Complexity:
- Iterating through the string takes O(n), where n is the length of the string.
- Summing up the counts in the dictionary takes O(m), where m is the number of unique characters.
- Therefore, the overall time complexity is O(n + m).

Space Complexity:
- The dictionary stores counts for each unique character in the string.
- In the worst case, the space complexity is O(m), where m is the number of unique characters.
"""
