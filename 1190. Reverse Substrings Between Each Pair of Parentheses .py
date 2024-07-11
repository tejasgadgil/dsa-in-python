class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Define a helper function to reverse the content within parentheses
        def reverseAndAppend():
            rev = []
            # Pop characters from the stack until an opening parenthesis is encountered
            while stack[-1] != "(":
                rev.append(stack.pop())
            # Pop the opening parenthesis
            stack.pop()
            # Extend the stack with the reversed content
            stack.extend(rev)
        
        # Convert the input string to a list for easier manipulation
        s = list(s)
        stack = []
        ptr = 0
        
        # Iterate through the input string
        while ptr < len(s):
            if s[ptr] == ')':
                # If a closing parenthesis is encountered, reverse the content within the parentheses
                reverseAndAppend()
            else:
                # Otherwise, push the character onto the stack
                stack.append(s[ptr])
            ptr += 1
        
        # Join the characters in the stack to form the final string
        return ''.join(stack)


# Explaination:
# push in stk till )
# pop and reverse from stack till (
# extend to stack
# continue till end of str
# stack to string

# Time Complexity
# O(n)
# Space Complexity
# O(n)
# Algorithm Approach
# Stack-based approach.
