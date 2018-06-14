




def insertionSort(alist):

    for index in range(1, len(alist)):
        print('changeing index to {i}'.format(i=index))

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:

            alist[position] = alist[position - 1]
            print('\t lst={lst}'.format(lst=alist))
            position = position - 1

        alist[position] = currentvalue
        print(alist)







alist = [54,26,93,17,77,31,44,55,20]
print(alist)
insertionSort(alist)
print(alist)


srtd_arr = [6, 5, 4, 3, 2, 1]
print(srtd_arr)
insertionSort(srtd_arr)
print(srtd_arr)



srtd_arr = [4, 3, 2, 1]
print(srtd_arr)
print('staring insertion_sort')
insertionSort(srtd_arr)
print(srtd_arr)
