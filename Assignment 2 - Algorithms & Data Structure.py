# Assignment 2
# Course: INFR 2820U - Algorithms & Data Structure
# Name: Mariyam Member
# Student Number: 100867858

import time
import winsound

# Merge Sort
def merge_sort_with_steps(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        print("Dividing array:", arr)
        print("Left half:", L)
        print("Right half:", R)

        merge_sort_with_steps(L)  # Sorting the first half
        merge_sort_with_steps(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                # Sound effect for swap
                winsound.Beep(1000, 100)
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print("Merging:", arr)

# Print the algorithm
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Original Array:", arr)
merge_sort_with_steps(arr)
print("Sorted Array:", arr)
