



'''
Quicksort doesnt check to see whether the input array is already sorted.
So it will still try to sort it.

O(n log n)
'''

def quicksort(array):
    #print('called... invoked function')
    if len(array) < 2:
        return array            # base case 1 or 0 elements in array
    else:
        pivot = array[0] #Recursive case
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        #print('about to partition')

        return quicksort(less) + [pivot] + quicksort(greater)


#orig_array = [10, 5, 2, 3, 100, 1]
#orig_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

orig_array = [10, 9, 8, 7, 6]

#print('orig array: {arr}'.format(arr=orig_array))


#print('sorted array usign qsort:')
print (quicksort(orig_array))

orig_array = [ 5, 4, 3, 2, 1]
print (quicksort(orig_array))


orig_array = [ 11, 12, 15, 18, 99]
print (quicksort(orig_array))


#sorted_arr = [1, 2, 3, 5, 10, 100]
#print(quicksort(sorted_arr))


#arr_with_ties = [10, 100, 3, 2, 99, 100, 100, 2, 2, 2, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#print(quicksort(arr_with_ties))
