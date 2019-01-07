

"""Naive implementation
"""
def bubble_sort(arr):

    for passnum in range(len(arr)-1, 0, -1):

        for idx in range(passnum):

            print('idx = {idx}, passnun={passnum}, arr = {arr}'.format(idx=idx, passnum=passnum, arr=arr))
            if arr[idx] > arr[idx+1]:
                # swap w/out a variable
                # result in two assignment statements being done at the same time
                arr[idx], arr[idx + 1] = arr[idx+1], arr[idx]

    return arr

#test_arr_rev = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#test_arr_rev = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(bubble_sort(test_arr_rev))


"""
    if during a pass, there are no exchanges then the list must be sorted.
    we can short-circuit the execution of bubble-sort by putting in a flag indicating such

"""
def bubble_sort_short(arr):
    exchanges = True
    for passnum in range(len(arr)-1, 0, -1):
        while exchanges:
            exchanges = False
            for idx in range(passnum):
                print('idx = {idx}, passnun={passnum}, arr = {arr}'.format(idx=idx, passnum=passnum, arr=arr))
                if arr[idx] > arr[idx+1]:
                    exchanges = True
                    arr[idx], arr[idx + 1] = arr[idx+1], arr[idx]
    return arr


test_arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bubble_sort_short(test_arr_sorted))




'''
    FIRST_TRY_ALMOST
    Ugh.... this was a first try but was wrong - close but wrong
    it resulted in way more passes than the traditional impl
    and failed to sort the first element when arr is in worst case/reverse order
'''

def bubble(arr):
    idx = 1
    while idx < len(arr):
        print('idx = {idx}, arr = {arr}'.format(idx=idx, arr=arr))
        if arr[idx-1] > arr[idx]:
            gt = arr[idx-1]
            arr[idx-1] = arr[idx]
            arr[idx] = gt
            idx = 1
        idx += 1

    return arr

test_arr_rev = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#print(bubble(test_arr_rev))