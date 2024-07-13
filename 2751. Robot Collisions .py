class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Combine positions, directions, and healths into a single list of tuples
        for i in range(n):
            positions[i] = [i, positions[i], directions[i], healths[i]]
        
        # Sort robots by their positions
        positions.sort(key=lambda positions: positions[1])

        stack = []
        i = 0
        
        while i < n:
            if len(stack) > 0 and stack[-1][2] == 'R' and positions[i][2] == 'L':
                if positions[i][3] == stack[-1][3]:
                    # If both robots have the same health, both are destroyed
                    stack.pop()
                    i += 1
                elif positions[i][3] > stack[-1][3]:
                    # If the incoming robot has more health, it survives but loses one health point
                    positions[i][3] -= 1
                    stack.pop()
                else:
                    # If the robot in the stack has more health, it survives but loses one health point
                    stack[-1][3] -= 1
                    i += 1
            else:
                # If there is no collision, add the current robot to the stack
                stack.append(positions[i])
                i += 1

        # Sort the remaining robots by their original index to return their health in the original order
        stack.sort(key=lambda stack: stack[0])
        newHealth = [robot[3] for robot in stack]

        return newHealth


# Time Complexity
# Sorting the robots by their positions takes O(nlogn), where n is the number of robots.
# The while loop processes each robot once, resulting in O(n) time complexity for this part.
# Sorting the stack by the original index takes O(nlogn).
# The total time complexity is O(nlogn).
  
# Space Complexity
# The space complexity is O(n) due to the stack and the additional list used to combine and sort the robot attributes.
  
# Algorithm Approach
# The algorithm approach used in this solution is a Greedy algorithm combined with a Stack-based approach.
