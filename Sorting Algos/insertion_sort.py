def insertionsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    print(arr)


if __name__ == '__main__':
    print('hello world!')
    arr = [19, 2, 31, 45, 30, 11, 121, 27]
    insertionsort(arr)