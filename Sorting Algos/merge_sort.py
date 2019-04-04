def mergesort(arr):
    if len(arr) <= 1:
        return (arr)
    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]

    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)

    return (merge(left_arr, right_arr))


def merge(left, right):
    total_len_new_arr = len(left) + len(right)
    new_arr = [0] * total_len_new_arr
    i = 0
    j = 0
    pntr = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            new_arr[pntr] = right[j]
            pntr += 1
            j += 1
        else:
            new_arr[pntr] = left[i]
            pntr += 1
            i += 1

    while i < len(left):
        new_arr[pntr] = left[i]
        pntr += 1
        i += 1

    while j < len(right):
        new_arr[pntr] = right[j]
        pntr += 1
        j += 1
    return (new_arr)


if __name__ == '__main__':
    print('yo')
    arr = [67, 3, 1, 6, 23, 0, -8, 7, 90]
    print(mergesort(arr))