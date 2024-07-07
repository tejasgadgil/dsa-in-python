class Solution(object):
    def numWaterBottles(self, numBottles, numEx):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        # Initialize the total count of bottles drunk to the number of bottles initially available
        drink = numBottles

        # Initialize the count of empty bottles to the number of bottles initially available
        empty = numBottles

        # Continue exchanging as long as the number of empty bottles is greater than or equal to the exchange rate
        while empty >= numEx:
            # Calculate the remainder when empty bottles are divided by the exchange rate
            isRemaining = empty % numEx
            
            # Calculate the number of new bottles obtained by exchanging empty ones
            empty = empty // numEx

            # Add the newly obtained full bottles to the total count of bottles drunk
            drink += empty

            # Update the count of empty bottles by adding the remaining empty bottles
            empty += isRemaining

        # Return the total count of bottles drunk
        return drink


# Time Complexity: The time complexity is O(log numEx(numBottles)). This is because in each iteration of the while loop, the number of empty bottles is divided by numEx, leading to a logarithmic reduction in the number of iterations required.
# Space Complexity: O(1). This is because the solution only uses a constant amount of extra space for the variables drink, empty, and isRemaining, regardless of the size of the input.
