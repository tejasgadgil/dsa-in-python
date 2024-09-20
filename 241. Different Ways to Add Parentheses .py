class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Dictionary to store available operations and their corresponding lambda functions
        operations = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y
        }

        # Recursive backtracking function to compute results for different parenthesizations
        def backtrack(left, right):
            res = []  # List to store results for the current subproblem

            # Iterate through the expression from left to right
            for i in range(left, right + 1):
                op = expression[i]  # Check for operator at the current index
                if op in operations:
                    # Recursively compute results for left and right sub-expressions
                    nums1 = backtrack(left, i-1)
                    nums2 = backtrack(i+1, right)

                    # Combine results from left and right sub-expressions using the current operator
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[op](n1, n2))
            
            # If no operator found, it means this is a single number, convert and return it
            if res == []:
                res.append(int(expression[left:right+1]))

            return res

        # Start backtracking for the entire expression
        return backtrack(0, len(expression)-1)


# Explanation:
# Algorithm/Approach: Recursive Divide and Conquer with Memoization.
# The algorithm uses recursion to evaluate all possible ways of parenthesizing the expression. 
# It recursively splits the expression at operators, computes the left and right parts, and combines 
# the results using the operators. If no operator is found, it returns the single number.

# Time Complexity:
# O(2^n * n), where:
# - n is the length of the expression.
# The recursion generates multiple combinations of sub-expressions (exponential growth in function calls), 
# and for each subproblem, we perform O(n) work in combining results. The exponential factor arises from 
# the fact that each operator can lead to multiple combinations of computations.

# Space Complexity:
# O(2^n), because:
# - The recursive call stack can grow to store intermediate results, and we store multiple combinations 
#   of sub-expressions in the result list. For n operators, there can be exponential possibilities.

# Summary:
# Time complexity: O(2^n * n)
# Space complexity: O(2^n)
