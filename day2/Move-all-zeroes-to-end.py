def move_zeros_to_end(arr):
    last_non_zero_index = 0  # Points to where the next non-zero should be placed

    # First pass: move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[last_non_zero_index] = arr[i]
            last_non_zero_index += 1

    # Second pass: fill remaining spaces with 0
    for i in range(last_non_zero_index, len(arr)):
        arr[i] = 0

    return arr

print(move_zeros_to_end([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros_to_end([10, 20, 30]))             # [10, 20, 30]
print(move_zeros_to_end([0, 0]))                   # [0, 0]
