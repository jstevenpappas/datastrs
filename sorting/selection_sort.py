'''

    Selection Sort



'''



def select_sort(arr):

    for fill_slot in range(len(arr)-1, 0, -1):

        position_max = 0

        for location in range(1, fill_slot + 1):

            if arr[position_max] < arr[location]:
                position_max = location


        print('fillslot={fs} position_max={pm}'.format(fs=fill_slot, pm=position_max))
        arr[fill_slot], arr[position_max] = arr[position_max], arr[fill_slot]
        print('new array: {new_arr}'.format(new_arr=arr))

    return arr




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





#input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print('Original Array= ', input)
#print(selection_sort(input))
print(select_sort(input))