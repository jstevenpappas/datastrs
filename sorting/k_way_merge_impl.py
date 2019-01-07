"""


"""

def merge_sort(input_list):

    if len(input_list) > 1:

        mid = len(input_list) // 2

        left_half = input_list[:mid]
        right_half = input_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_idx = 0
        right_idx = 0
        list_idx = 0

        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                input_list[list_idx] = left_half[left_idx]
                left_idx = left_idx + 1
            else:
                input_list[list_idx] = right_half[right_idx]
                right_idx = right_idx + 1
            list_idx = list_idx + 1

        # append remainder of left half to list
        while left_idx < len(left_half):
            input_list[list_idx] = left_half[left_idx]
            left_idx = left_idx + 1
            list_idx = list_idx + 1

        # append remainder of right half to list
        while right_idx < len(right_half):
            input_list[list_idx] = right_half[right_idx]
            right_idx = right_idx + 1
            list_idx = list_idx + 1

    return input_list




def k_way_merge(*lists):
    # implemented by k-way partition
    k = len(lists)
    if k > 1:
        mid = int(k / 2)
        B = k_way_merge(*lists[0: mid])
        C = k_way_merge(*lists[mid:])
        A = merge(B, C)
        return A
    return lists[0]


def merge(B, C):

    ret_list = []
    b_len = len(B)
    c_len = len(C)
    b_idx = 0
    c_idx = 0

    while b_idx < b_len and c_idx < c_len:
        if B[b_idx] <= C[c_idx]:
            ret_list.append(B[b_idx])
            b_idx += 1
        else:
            ret_list.append(C[c_idx])
            c_idx += 1

    for b in B[b_idx:]:
        ret_list.append(b)

    for c in C[c_idx:]:
        ret_list.append(c)


    return ret_list


if __name__ == '__main__':

    single_list = [3, 33, 1, 2, 4, 9, 5, 19, 35, 21, 8]

    print('Unsorted input: {us}'.format(us=single_list))

    x = merge_sort(single_list)
    print('Merge Sort on unsorted list: {sl}'.format(sl=x))

    print('')

    input_lists = [[1, 3, 5], [2, 4, 6, 200, 300, 400, 500, 555], [7, 8, 10], [11, 13], [12, 14, 101, 102]]

    print('Presorted lists to be sorted and merged vi K-Way Merge: {il}'.format(il=input_lists))

    merged_lists = k_way_merge(*input_lists)
    print('K-Way Merge on multiple presorted lists: {ml}'.format(ml=merged_lists))
