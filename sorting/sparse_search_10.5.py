"""Sparse Search.

Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.

E.g.,

Input:  ball, ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
Ouput: 4
"""



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


print(get_loc_sparse_search(arr, target))



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