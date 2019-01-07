"""Sparse Search.

Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.

E.g.,

Input:  ball, ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
Ouput: 4
"""



'''
Discussion.

problem 10.5 p. 401

She over-complicates this problem.

She correctly states that were it not for the empty strings, we could use binary search.
However she presents a modified version of binary search to solve this issue.
The runtime can never be better than O(n) (i.e., the len/sz of the array).


A curve is thrown at the end of the problem where she states 'what if someone searches for
and empty string? is it an error or do we return the first position of an empty string?'

### Empty string as valid input ###
This is a good question left to the interviewer. 
 
If it was the case where an empty string is valid input we would need to add an 'else' 
clause to the if statement testing if the target was empty and the curr element were empty
then we return the location.

If an empty string was not valid input, then we would leave the method as is.

'''



def binary_search_sparse(arr_of_strings, target, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2

    print('Element {} found at following idx: {}'.format(arr_of_strings[mid], mid))

    # is our first attempt empty?
    if not arr_of_strings[mid]:
        print('element between pipes |{}| is empty at index {}'.format(arr_of_strings[mid], mid))

        # search for next non-empty string
        left = mid - 1
        right = mid + 1

        while True:
            print('While loop left={} and right={} and current guess == {}'.format(left, right, arr_of_strings[mid]))

            if left < start and right > end:
                return -1 # cause we are beyond our bounds

            elif left >= start and arr_of_strings[left] != "":
                print('left >= start and guess is not empty: ', arr_of_strings[left])
                mid = left
                break

            elif right <= end and arr_of_strings[right] != "":
                print('right <= start and guess is not empty: ', arr_of_strings[right])
                mid = right
                break

            # -> increment the right by 1
            right = right + 1
            # -> decrement the left by 1
            left = left - 1

    ###
    # now do the comparisons and recurse if necessary
    ###
    print('current guess = {}'.format(arr_of_strings[mid]))

    if arr_of_strings[mid] == target:
        return mid

    elif arr_of_strings[mid] > target:  # too high so search left
        print('\ttoo high')
        return binary_search_sparse(arr_of_strings, target, start, mid-1)

    elif arr_of_strings[mid] < target:
        print('\ttoo low')
        return binary_search_sparse(arr_of_strings, target, mid+1, end)



def search_sparse_arr(string_arr, target):
    if len(string_arr) == 0 or not target:
        return -2
    else:
        start_idx = 0
        end_idx = len(string_arr) - 1
        return binary_search_sparse(string_arr, target, start_idx, end_idx)





arr = ["at", "", "", "", "ball", "", "bbb", "car", "", "", "dad", "", "", "suckit"]
#target = "suckit"
target = "dad"
idx_target = search_sparse_arr(arr, target)

print('The target {tar} occurs at the following index in the array: {idx}'.format(tar=target, idx=idx_target))


def get_loc_sparse_search(arr, target):
    targ_loc = None # indicator to signify not found
    alen = len(arr)
    for i in range(alen):
        curr = arr[i]
        if curr is not None:
            if curr == target:
                targ_loc = i
    return targ_loc


arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
target = "balll"


#print(get_loc_sparse_search(arr, target))
