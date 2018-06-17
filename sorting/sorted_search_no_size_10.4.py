


'''

    Sorted Search no Size

    We have an array-like structure Listy that lacks a size method.
    It does however have an  elementAt(i) method that returns the element at index i in
    O(1) time.
    If i is beyond the bounds of the datastructure, it returns -1.
    (For this reason, the data structure only supports positive integers.)

    Given a Listy which contains sorted, positive integers, find the index at which an element X occurs.
    If X occurs multiple times, you may return any index.

    Hints:
        320: Think about how binary search works.
             What will be the issue with just implementing binary search?

        337: Binary search requires comparing an element to the midpoint.
             Getting the midpoint requires knowing the length.
             We don't know the length.  Can we find it?

        348: We can find the length by using an exponential backoff.
             First check index 2, then 4, then 16 and so on.
             What will be the runtime of this algorithm?
'''



'''
    Here, we find the size of an array without a length() method
    
    Instead of linearly searching through the array, we jump the index by 2 each time
    changing the search from O(N) to O(logN) 
    
    1 function to return the bounds of the index where the target value falls.
    A second function which is a modified version of binary search to look for the
    value in the array and return its index when found
    
    Not knowing the length of the array didn't impact the runtime:
        O(logN) for search

'''

class Listy(object):
    def __init__(self, arr):
        self.arr = arr

    def elementAt(self, idx):
        try:
            return self.arr[idx]

        except IndexError:
            return -1




def search_(listy, target):
    # start the index at 1
    idx = 1
    while listy.elementAt(idx) != -1 and listy.elementAt(idx) < target:
        # if we are out of bounds or the current element is less than
        # the target element, then backoff exponentially and increase
        # the index by doubling it each time (i.e., 2, 4, 8, 16, etc.)
        idx = idx * 2

    return binary_search(listy, target, idx//2, idx)



def binary_search(listy, target, low, high):

    while low <= high:

        mid = (low + high) // 2

        guess = listy.elementAt(mid)

        if guess > target or guess == -1:
            high = mid -1

        elif guess < target:
            low = mid +1

        else:
            return mid




targ = 5
arr = [0, 2, 4, 5, 6, 8, 9, 11, 15, 99, 100, 108]

ls = Listy(arr)

print(search(ls, targ))