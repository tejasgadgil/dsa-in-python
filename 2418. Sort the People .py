from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Partition function for quicksort
        def partition(heights, names, low, high):
            pivot = heights[high]  # Choose the last element as pivot
            i = low - 1
            for j in range(low, high):
                if heights[j] >= pivot:  # Change condition to sort in descending order
                    i = i + 1
                    (heights[i], heights[j]) = (heights[j], heights[i])
                    (names[i], names[j]) = (names[j], names[i])
            (heights[i + 1], heights[high]) = (heights[high], heights[i + 1])
            (names[i + 1], names[high]) = (names[high], names[i + 1])
            return i + 1
        
        # Quicksort function
        def quicksort(heights, names, low, high):
            if low < high:
                pivot = partition(heights, names, low, high)
                quicksort(heights, names, low, pivot - 1)
                quicksort(heights, names, pivot + 1, high)
        
        quicksort(heights, names, 0, len(heights) - 1)
        return names  # Return names in descending order of heights

# Approach: Quick Sort
# Time Complexity: The average-case time complexity of quicksort is O(nlogn). However, in the worst case (when the pivot is always the smallest or largest element), it can degrade to O(n^2).
# Space Complexity: Quicksort is an in-place sorting algorithm, so it uses O(logn) space on the call stack due to recursion.
