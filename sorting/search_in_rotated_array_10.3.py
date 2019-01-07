




def bin_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:

        midpoint = (low + high) // 2

        guess = list[midpoint]

        if guess == target:
            return midpoint

        elif guess < target:
            low = midpoint + 1

        else:
            high = midpoint - 1








'''
    Problem w/ below (from SE) is that you get
    'IndexError: list index out of range' if you
    pass in a sorted array
'''
def find_pivot_rotated_arr_wrong(arr):
    for ele_idx in range(0, len(arr), 1):
        if arr[ele_idx+1] < arr[ele_idx ]:
            return ele_idx



'''
    Belows find_pivot...() will return 'None' if
    sorted array is passed in, otherwise
    it will return index of pivot point
    (i.e., idx of # that is lt # preceding it)
'''
def find_pivot_rotated_arr(arr):
    for ele_idx in range(0, len(arr), 1):
        if ele_idx > 0 and arr[ele_idx-1] > arr[ele_idx]:
            # return idx where sorted subarray this is the start of the next array
            return ele_idx


def get_piv(arr):

    for i in range(len(arr)):
        if i > 0 and arr[i-1] > arr[i]:
            return i


arr_rot = [5, 6, 7, 8, 1, 2, 3, 4]

piv = get_piv(arr_rot)

lsr_half = arr_rot[piv:]
grt_half = arr_rot[:piv]


max_lsr = lsr_half[len(lsr_half) - 1]
min_gtr = grt_half[0]


tar = 3

if tar <= max_lsr:
    print(bin_search(lsr_half, tar) + len(grt_half))

elif tar >= min_gtr:
    print(bin_search(grt_half, tar))


print('BREAK')



def bin_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:

        midpoint = (low + high) // 2

        guess = list[midpoint]

        if guess == target:
            return midpoint

        elif guess < target:
            low = midpoint + 1

        else:
            high = midpoint - 1










# rotated array
arr_rot = [5, 6, 7, 8, 1, 2, 3, 4]

# sorted array - for testing with both versions
#arr_rot = [0, 1, 2, 3, 4, 5, 6, 7]

piv = find_pivot_rotated_arr(arr_rot)
print(find_pivot_rotated_arr(arr_rot))




# using the pivot we slice the list into 2 sorted subarrays

target = 6


arr1 = arr_rot[:piv]    # arr w/ lsr ele
arr2 = arr_rot[piv:]    # arr w/ gtr ele
print(arr1)
print(arr2)

max_arr1 = max(arr1)
max_arr2 = max(arr2)




if piv is not None:

    if max_arr1 > max_arr2:
        lsr_max = max_arr2
        arr_with_higher_vals = arr1
        arr_with_lesser_vals = arr2
    else:
        lsr_max = max_arr1
        arr_with_higher_vals = arr2
        arr_with_lesser_vals = arr1


    if target > lsr_max:
        print(bin_search(arr_with_higher_vals, target))
    else:
        idx_subarr = (bin_search(arr_with_lesser_vals, target))
        print(idx_subarr + len(arr_with_higher_vals))

else:
    print(bin_search(arr_rot, target))


