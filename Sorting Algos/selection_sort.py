def selectionsort(arr):
    for i_outer in range(0, len(arr) - 1):
        i_min = i_outer
        for i in range(i_outer, len(arr) - 1):
            if arr[i_min] > arr[i]:
                i_min = i
        arr[i_min], arr[i_outer] = arr[i_outer], arr[i_min]
    print(arr)


if __name__ == '__main__':
    arr = [67, 3, 1, 6, 23, 0, -8, 7, 90]
    selectionsort(arr)