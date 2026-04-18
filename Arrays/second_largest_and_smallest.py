# Problem: Find second largest and second smallest elements in an array
# Approach: Single traversal updating largest, second largest,
# smallest and second smallest simultaneously
# Example: [1, 2, 4, 7, 7, 5]
# Output: second largest = 5, second smallest = 2
# Time Complexity: O(n)
# Space Complexity: O(1)

def getSecondOrderElements(n, a):

    largest = float("-inf")
    second_largest = float("-inf")

    smallest = float("inf")
    second_smallest = float("inf")

    for i in range(n):

        # Update largest and second largest
        if a[i] > largest:
            second_largest = largest
            largest = a[i]

        elif a[i] > second_largest and a[i] != largest:
            second_largest = a[i]

        # Update smallest and second smallest
        if a[i] < smallest:
            second_smallest = smallest
            smallest = a[i]

        elif a[i] < second_smallest and a[i] != smallest:
            second_smallest = a[i]

    return second_largest, second_smallest


# Example test
print(getSecondOrderElements(6, [1, 2, 4, 7, 7, 5]))
