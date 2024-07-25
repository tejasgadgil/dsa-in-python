class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # This function merges two sorted subarrays into one sorted array
        def merge(arr, l, m, r):
            # Create temporary arrays for left and right subarrays
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = 0, 0, l

            # Merge the two temporary arrays back into the original array
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Copy any remaining elements of left[], if any
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            # Copy any remaining elements of right[], if any
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        # This function recursively divides the array and merges the sorted halves
        def mergeSort(arr, l, r):
            if l < r:
                # Find the middle point to divide the array into two halves
                m = (l + r) // 2
                # Recursively sort the first half
                mergeSort(arr, l, m)
                # Recursively sort the second half
                mergeSort(arr, m + 1, r)
                # Merge the sorted halves
                merge(arr, l, m, r)
            return arr

        # Call the mergeSort function on the entire array
        return mergeSort(nums, 0, len(nums) - 1)


# Approach
# The approach used here is Merge Sort, which is a classic divide-and-conquer sorting algorithm.
# Time Complexity: 
# O(nlogn)
# Space Complexity
# O(n) 





