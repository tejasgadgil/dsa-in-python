class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def addToList(elements, i):
            if formula[i] == '(':
                elements.append(['(', 1])
            elif formula[i].isupper():
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                element = formula[i:j]
                k = j
                while k < len(formula) and formula[k].isdigit():
                    k += 1
                count = int(formula[j:k]) if j != k else 1
                elements.append([element, count])
                return k - i
            elif formula[i] == ')':
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                count = int(formula[i + 1:j]) if i + 1 != j else 1
                elements.append([')', count])
                return j - i
            return 1

        # phase 1: separate
        elements = []
        formula = '(' + formula + ')'
        i = 0
        while i < len(formula):
            i += addToList(elements, i)
        # print(elements)

        # phase 2: open brackets
        stack = list()
        i = 0
        while i < len(elements):
            if elements[i][0] != ')':
                stack.append(elements[i])
                i += 1
            else:
                mul = int(elements[i][1])
                j = -1
                while stack[j][0] != '(':
                    stack[j][1] *= mul
                    j -= 1
                stack.pop(j)
                i += 1
                
        # phase 3: sort
        stack.sort()
        
        # phase 4: add together and join
        result = list()
        result.append(stack[0])
        i = 1
        while i < len(stack):
            if result[-1][0] != stack[i][0]:
                result.append(stack[i])
                i += 1
            else:
                result[-1][1] += stack[i][1]
                i += 1

        resultStr = ''
        for ele in result:
            if ele[1] == 1:
                resultStr += ele[0]
            else:
                resultStr += ele[0] + str(ele[1])
            
        return resultStr



# Time Complexity
# The algorithm involves multiple passes over the input string and lists, contributing to linear time complexity relative to the length of the formula.
# The sorting step adds a complexity of O(nlogn), where n is the number of distinct elements in the formula.
# Overall, the time complexity is O(nlogn).
  
# Space Complexity
# The space complexity is O(n), where n is the length of the formula due to the storage requirements for the elements list and stack.
  
# Algorithm Approach
# This algorithm uses a Stack-Based Parsing approach:
# It parses the formula into manageable parts and processes parentheses and multipliers effectively using a stack.
# By handling elements and multipliers separately and then combining them, it ensures accurate counts and correctly formatted output.
