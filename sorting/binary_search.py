




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


