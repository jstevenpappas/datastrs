

def insertion_sort(alist):

    for index in range(1, len(alist)):

        current_value = alist[index]

        position = index

        while position > 0 and alist[position - 1] > current_value:

            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = current_value





alist = [54,26,93,17,77,31,44,55,20]
print(alist)
insertion_sort(alist)
print(alist)


srtd_arr = [6, 5, 4, 3, 2, 1]
print(srtd_arr)
insertion_sort(srtd_arr)
print(srtd_arr)



srtd_arr = [4, 3, 2, 1]
print(srtd_arr)
print('staring insertion_sort')
insertion_sort(srtd_arr)
print(srtd_arr)
