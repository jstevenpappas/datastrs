

'''

    Selection Sort



'''
def selection_sort(arr):

    for fill_slot in range(len(arr)-1, 0, -1):
        position_max = 0

        for location in range(1, fill_slot + 1):
            #print('location = {location}, fill_slot={fill_slot}, position_max={position_max}, arr = {arr}'.format(
            #    location=location, fill_slot=fill_slot +1, position_max=position_max, arr=arr))

            if arr[location] > arr[position_max]:
                #print('setting max from {prev_pos_max} to {curr_pos_max}'.format(prev_pos_max=position_max,
                #                                                                 curr_pos_max=location))
                position_max = location

        #arr[fill_slot], arr[position_max] = arr[position_max], arr[fill_slot]
        arr[fill_slot], arr[position_max] = arr[position_max], arr[fill_slot]

    return arr







test_arr_rev = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print('arr = ', test_arr_rev)
print(selection_sort(test_arr_rev))

print('')

#test_arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8]
test_arr_sorted = [5, 6, 7, 8, 1, 2, 3, 4]

#print('arr = ', test_arr_sorted)
#print(test_arr_sorted)


#tst_arr = [4, 3, 2, 1]

tst_arr = [2, 1, 4, 3]

print('arr = ', tst_arr)
print(selection_sort(tst_arr))

