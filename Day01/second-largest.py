def get_second_largest(arr):
    if len(arr) < 2:
        return -1  # Not enough elements for second largest

    first = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else -1


print(get_second_largest([2, 3, 1, 5, 6]))  # Output: 5
print(get_second_largest([10, 10, 10]))     # Output: -1 (all same)
print(get_second_largest([5]))               # Output: -1 (only one element)
print(get_second_largest([-2, -3, -1, -5])) # Output: -2 (works with negatives)
