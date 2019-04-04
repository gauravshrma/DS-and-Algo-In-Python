def shellsort(arr):
    gap = len(arr)//2
    while gap>0:
        for i in range(gap,len(arr)):
            j = i - gap
            temp = arr[i]
            while j>=0 and arr[j]>temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = gap//2
    print(arr)

if __name__ == '__main__':
    print('hello world!')
    arr = [19,2,31,45,30,11,121,27]
    shellsort(arr)