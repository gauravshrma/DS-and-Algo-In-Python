def quick_sort(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)
        quick_sort(arr, first, splitpoint - 1)
        quick_sort(arr, splitpoint + 1, last)


def partition(arr, left, right):
    pivotval = arr[left]
    left_iter = left + 1
    right_iter = right

    while True:
        while pivotval > arr[left_iter] and left_iter <= right_iter:
            left_iter += 1
        while pivotval < arr[right_iter] and left_iter <= right_iter:
            right_iter -= 1

        if left_iter < right_iter:
            arr[left_iter], arr[right_iter] = arr[right_iter], arr[left_iter]
        else:
            break
    arr[left], arr[right_iter] = arr[right_iter], arr[left]

    return (right_iter)


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    first = 0
    last = len(arr) - 1
    quick_sort(arr, first, last)
    print(arr)