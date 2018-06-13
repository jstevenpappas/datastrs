
'''


Like QuickSort, Merge Sort is a Divide and Conquer algorithm.

It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

The merge() function is used for merging two halves.

The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r]
are sorted and merges the two sorted sub-arrays into one.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

'''
# result = [0] * len(arr)





def merge(arr, left, mid, right):
    print('    left={left}'.format(left=left))
    print('    right={right}'.format(right=right))
    print('    mid={mid}'.format(mid=mid))

    n1 = mid - left + 1
    n2 = right - mid

    # create tmp arrays
    L = [0] * n1
    R = [0] * n2

    # copy data into temp subarrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # merge temp subarrays L[] and R[] back into arr[left...right]
    i = 0 # idx first subarray
    j = 0 # idx second subarray
    k = left # idx of resultant merged array

    while i < n1 and j < n2:
        print(arr)
        print(L)
        print(R)

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    # copy any remaining elements of L[] if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k +=1

    # same for right array R[]
    while j < n2:
        arr[k] =  R[j]
        j += 1
        k +=1


def merge_sort(arr, left, right):
    print('left={left}'.format(left=left))
    print('right={right}'.format(right=right))
    if left < right:

        mid = (left + (right - 1)) // 2
        print('Mmid={mid}'.format(mid=mid))

        # sort the first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)






arr = [12, 11, 13, 5, 6, 7]

arr_len = len(arr)

print(arr)

merge_sort(arr, 0, arr_len -1)

print(arr)




