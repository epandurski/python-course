def mergesort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        center = (left + right) // 2
        mergesort(arr, left, center)
        mergesort(arr, center + 1, right)
        merge(arr, left, center, right)


def merge(arr, left, center, right):
    n_left, n_right = center - left + 1, right - center
    L = [arr[left + i] for i in range(n_left)]
    R = [arr[center + 1 + j] for j in range(n_right)]
    i, j, k = 0, 0, left  # initial indexes
    while i < n_left and j < n_right:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n_left:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n_right:
        arr[k] = R[j]
        j += 1
        k += 1


# code to test the above
arr = [12, 11, 13, 5, 6, 7]
mergesort(arr)
print(arr)
