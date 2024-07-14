class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit to 0
        profit = 0
        
        # Initialize two pointers l (left) and r (right) to the start of the array
        l = r = 0
        
        # Iterate through the prices array
        while r < len(prices):
            # If the current price at r is less than the price at l, move l to r
            if prices[r] < prices[l]:
                l = r
                r += 1
            # If the current price at r is greater than or equal to the price at l
            elif prices[r] >= prices[l]:
                # Calculate the potential profit and update the maximum profit if needed
                profit = max(profit, prices[r] - prices[l])
                r += 1
                
        # Return the maximum profit found
        return profit

# Time Complexity
# O(n)
# Space Complexity
# O(1).
# Algorithm Approach
# Two Pointers approach
