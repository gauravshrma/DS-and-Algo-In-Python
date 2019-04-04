def bubblesort(arr):

    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

if __name__ == '__main__':
    print('Initiating the program...\n')
    arr = [67, 3, 1, 6, 23, 0, -8, 7, 40]
    bubblesort(arr)