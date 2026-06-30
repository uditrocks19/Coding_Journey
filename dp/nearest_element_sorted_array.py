def search_nearest(arr, x):
    s, end = 0, len(arr) - 1

    while s <= end:
        mid = (s + end) // 2

        # If we find the exact element, return it
        if arr[mid] == x:
            return arr[mid]

        # Narrow the search range
        if arr[mid] < x:
            s = mid + 1
        else:
            end = mid - 1

    # After exiting the loop, `s` and `end` represent the bounds around `x`
    # Check which of `arr[s]` or `arr[end]` is closer to `x`
    if s < len(arr) and (end < 0 or abs(arr[s] - x) < abs(arr[end] - x)):
        return arr[s]
    return arr[end]

# Example usage
arr = [1, 3, 5, 7, 9]
x = 6
print(search_nearest(arr, x))  # Output: 5 (nearest to 6)
