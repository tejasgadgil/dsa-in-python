class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create a set to store all allowed characters
        consistent = set(allowed)
        
        # Initialize the count of consistent words as the total number of words
        cons_words = len(words)
        
        # Loop through each word in the words list
        for word in words:
            # Check each character in the word
            for i in word:
                # If a character is not in the allowed set, decrement the count and break
                if i not in consistent:
                    cons_words -= 1
                    break
        
        # Return the number of consistent words
        return cons_words


# Algorithm/Approach: HashSet and String Traversal.
# Time complexity: O(n×m)
# Space complexity: O(a)
