class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Initialize the time when the chef finishes the current order
        doneAt = 0
        
        # Initialize the total waiting time
        waitTime = 0

        # Iterate through the list of customers
        for cust in customers:
            # Calculate the time when the current customer's order is completed
            # It is the maximum of the current doneAt time and the customer's arrival time, plus the preparation time
            doneAt = max(doneAt, cust[0]) + cust[1]
            
            # Add the waiting time for the current customer to the total waiting time
            # Waiting time is the difference between the order completion time and the customer's arrival time
            waitTime += (doneAt - cust[0])

        # Calculate and return the average waiting time
        return waitTime / len(customers)


# [[1,2],[2,5],[4,3]]
#   0<1   3>2   8>4
#   1+2   3+5   8+3
#    3     8    11   --> doneAt
#   3-2    8-5   11-3 --> waitTime total


# Time Complexity
# O(n)
# Space Complexity
# O(1)
# Algorithm
# The greedy nature of this algorithm is evident in its focus on making the best immediate choice (starting the next order as soon as possible) without needing to plan for future customers.
