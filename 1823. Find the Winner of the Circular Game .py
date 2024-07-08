class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize the circle with people labeled from 0 to n-1
        circle = list(range(n))
        
        # Adjust k to be zero-based for easier calculations
        k = k - 1
        cur = 0

        # Eliminate every k-th person until only one person is left
        while n > 1:
            # Calculate the index of the person to eliminate
            cur = (cur + k) % n
            # Remove the person from the circle
            circle.pop(cur)
            # Decrease the number of people in the circle
            n -= 1

        # Return the position of the last remaining person (convert to one-based index)
        return circle[0] + 1


# Iterative Soln
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         winner = 0
#         for i in range(2, n + 1):
#             winner = (winner + k) % i
#         return winner + 1  # Convert zero-based index to one-based index

# Recursive Soln
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         return self.findWinner(n, k) + 1  # Convert zero-based index to one-based index

#     def findWinner(self, n: int, k: int) -> int:
#         if n == 1:
#             return 0  # Base case: only one person left
#         else:
#             return (self.findWinner(n - 1, k) + k) % n  # Recursive step


# My Code (Using List):
# Time Complexity: 
# O(n^2)
# Space Complexity: 
# O(n)
# Optimized Iterative Version:
# Time Complexity: 
# O(n)
# Space Complexity: 
# O(1)
# Recursive Version:
# Time Complexity: 
# O(n)
# Space Complexity: 
# O(n)

