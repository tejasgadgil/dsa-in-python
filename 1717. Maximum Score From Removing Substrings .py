class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Helper function to remove pairs and calculate the score
        def removePairs(s, c1, c2, score):
            stack = []
            tmpScore = 0
            # Iterate through each character in the string
            for char in s:
                # If the top of the stack is c1 and the current character is c2, remove the pair
                if stack and stack[-1] == c1 and char == c2:
                    stack.pop()
                    tmpScore += score
                else:
                    stack.append(char)
            # Return the score for removed pairs and the remaining string
            return tmpScore, ''.join(stack)

        score = 0
        # Choose the order of removing pairs based on which pair has a higher score
        if x > y:
            # Remove 'ab' pairs first
            score1, s = removePairs(s, 'a', 'b', x)
            # Then remove 'ba' pairs
            score2, s = removePairs(s, 'b', 'a', y)
        else:
            # Remove 'ba' pairs first
            score1, s = removePairs(s, 'b', 'a', y)
            # Then remove 'ab' pairs
            score2, s = removePairs(s, 'a', 'b', x)
        
        # Return the total score
        return score1 + score2


# locate higher scored pair using top of stack and string, score, repeat for lower scored pair

# Time Complexity
# O(n)
# Space Complexity
# O(n)
# Algorithm Approach
# Greedy algorithm with a Stack-based approach.


# MY BRUTEFORCE APPROACH
        # def lookFor(look):
        #         i = len(s)-1
        #         locateArr = list()
                
        #         while(i > 0):
        #             if (s[i-1] + s[i]) == look :
        #                 locateArr.append(i-1)
        #             i -= 1
                
        #         return locateArr

        # def dissolveAndScore(locateArr, add, score):
        #     for index in locateArr:
        #             s.pop(index)
        #             s.pop(index)
        #             score += add
        #     return score

        # if x > y :
        #     look1 = "ab"
        #     look2 = "ba"
        #     score1 = x
        #     score2 = y
        # else :
        #     look1 = "ba"
        #     look2 = "ab"
        #     score1 = y
        #     score2 = x
        
        # s = list(s)
        # score = 0
        # # if x > y :
        # count1 = 100
        # count2 = 100
        # while(count1 != 0 or count2 != 0) : 
        # # repeat till none left of both
        #     # till none left
        #     while(count1 != 0) :
        #         location1 = lookFor(look1)
        #         count1 = len(location1)
        #         score = dissolveAndScore(location1, score1, score)
        #         # print(s, " ", score, " countab ", " ", count1)

        #     # once
        #     location2 = lookFor(look2)
        #     count2 = len(location2)
        #     score = dissolveAndScore(location2, score2, score)
        #     # print(s, " ", score, " countba ", " ", count2)

