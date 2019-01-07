




'''

    O(logN)


'''


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


def b_search(input_list, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        guess = input_list[mid]

        if guess == target:
            return mid

        else:
            if guess < target:
                b_search(input_list, target, mid+1, end)

            else:
                b_search(input_list, target, start, mid-1)

    return None







# iterative form
ordered_array = [11, 33, 49, 99, 101, 213, 332, 444, 555, 654, 1000]
search_target = 213
print(bin_search(ordered_array, search_target))


# recursive form
ordered_array_rec = [11, 33, 49, 99, 101, 213, 332, 444, 555, 654, 1000]
search_target_rec = 213
start = 0
end = len(ordered_array_rec) - 1

print(b_search(ordered_array_rec, search_target_rec, start, end))


