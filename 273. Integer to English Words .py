class Solution:
    def numberToWords(self, num: int) -> str:
        """
        This method converts a number into its English words representation.
        """
        if num == 0:
            return "Zero"

        # Mappings of numbers to their word equivalents for ones and teens.
        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        # Mappings of tens to their word equivalents.
        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def get_str(n):
            """
            This helper method converts a number less than 1000 into its English words representation.
            """
            block = []
            hundred = n // 100
            if hundred:
                block.append(ones_map[hundred] + " Hundred")
            last_two = n % 100
            if last_two >= 20:
                tens = last_two // 10
                ones = last_two % 10
                block.append(tens_map[tens * 10])
                if ones:
                    block.append(ones_map[ones])
            elif last_two > 0:
                block.append(ones_map[last_two])

            return " ".join(block)

        postfix = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []

        # Process each block of 1000.
        while num:
            digits = num % 1000
            s = get_str(digits)
            if s:
                res.append(s + postfix[i])
            num = num // 1000
            i += 1

        res.reverse()
        return " ".join(res)

# Algorithm/Approach: Divide and Conquer with Mapping and Modulo Operation
#
# Time Complexity: O(log n)
# - The number of iterations is proportional to the number of digits in the number (base 1000), which is log10(n).
# - The conversion within each 3-digit block is constant time O(1) since the number of operations within the block is fixed.
# - Therefore, the overall time complexity is O(log n), where n is the input number.
#
# Space Complexity: O(1)
# - The space complexity is constant, O(1), since the space used by the helper data structures (ones_map, tens_map, and postfix) does not scale with the input size.
# - The only additional space used is for the result list, which is proportional to the number of blocks (log n), but this is still considered constant relative to the input size.
