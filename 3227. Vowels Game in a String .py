class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Define a set of vowels
        vowels = {"a", "e", "i", "o", "u"}
        
        # Initialize a counter for vowels
        vcount = 0
        
        # Iterate over each character in the string
        for i in s:
            # If the character is a vowel, increment the counter
            if i in vowels:
                vcount += 1
        
        # If there are no vowels, Alice loses
        if vcount == 0:
            return False
        
        # If there is at least one vowel, Alice wins
        return True

"""
Time Complexity:
- The iteration over the string takes O(n), where n is the length of the string.
- Checking membership in a set takes O(1) on average.
- Overall, the time complexity is O(n).

Space Complexity:
- The set of vowels is a fixed size of 5, so it takes O(1) space.
- The counter and a few variables also take O(1) space.
- Overall, the space complexity is O(1).
"""
