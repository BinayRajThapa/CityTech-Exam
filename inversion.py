def count_inversions(arr):
    # Helper function to merge two halves of the array and count inversions
    def merge_and_count(arr, temp_arr, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        inv_count = 0
        inv_count += merge_and_count(arr, temp_arr, left, mid)
        inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
        return inv_count

    # Merge function to merge two halves and count inversions
    def merge(arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                j += 1
            k += 1

        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into Original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
        
        return inv_count

    # Initialize a temporary array and call the helper function
    n = len(arr)
    temp_arr = [0] * n
    return merge_and_count(arr, temp_arr, 0, n - 1)

# Example usage:
arr = [1, 20, 6, 4, 5]
result = count_inversions(arr)
print("Total inversions:", result)
