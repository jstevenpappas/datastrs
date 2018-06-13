





def merge_sorted(array_a, array_b, num_elements_a, num_elements_b):

    a_idx = num_elements_a - 1          # last idx of array A
    b_idx = num_elements_b - 1          # last idx of array B
    idx_merged = num_elements_a + num_elements_b -1   # last idx of merged array

    print(' a_idx={a} b_idx={b} idx_merged={idx}'.format(a=a_idx, b=b_idx, idx=idx_merged))


    while b_idx >= 0:

        if a_idx >= 0 and array_a[a_idx] > array_b[b_idx]:

            array_a[idx_merged] = array_a[a_idx]
            a_idx = a_idx -1

        else:
            array_a[idx_merged] = array_b[b_idx]
            b_idx = b_idx -1

        idx_merged = idx_merged -1

    return array_a

'''

because we represent the 'space at the end of Array A with elements = 0
we just can't pass in len(arr_a) below and have to count the elements with
valid values...   kind of a pyhto


'''



arr_a = [5, 6, 7, 8, 9, 0, 0, 0]
len_valid_ele_in_a = len([i for i in arr_a if i > 0])


arr_b = [3, 4, 5]
len_valid_ele_in_b = len([i for i in arr_b if i > 0])


merge_sorted(arr_a, arr_b, len_valid_ele_in_a, len_valid_ele_in_b)

print(arr_a)

