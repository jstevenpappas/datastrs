
from collections import defaultdict

"""
One Away
    There are 3 types of edits that can be performed on strings: insert a char,
    remove a char, replace a char.
    Given 2 strings, write a function to check if they are one edit (or zero edits) away.
    
    Example:

        pale, ple -> true
        pales, pale -> true
        pale, bale -> true
        pale, bake -> false

"""

'''
case replace:
    both strings need to be same size
case insert/remove:
    1 string would need to be 1 char less than the other to be eligible
'''


def is_one_edit_away(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    # if the same len, use the replace() function
    if len1 == len2:
        return is_one_edit_replace(str1, str2)
    else:
        # if diff lengths, use the add_remove() function but pass in
        # the shorter string first
        if (len1+1) == len2:
            return is_one_add_remove_away(str1, str2)
        elif (len1-1) == len2:
            return is_one_add_remove_away(str2, str1)

"""
is one replace away:

since the strings are the same len, they have to be different in exactly 1 place
so iterate over both and count the number of times they are unequal.

If it is 1, then True - they are one char replacement away.

if it is more than 1 or 0 then they are the same string or 
more than one replacement away

"""


def is_one_edit_replace(str1, str2):
    print('str1 = {s1}, str2 = {s2}'.format(s1=str1, s2=str2))
    diff_cnt = 0
    for idx in range(len(str1)):
        print(idx)
        if str1[idx] != str2[idx]:
            diff_cnt += 1
    if diff_cnt == 1:
        return True
    else:
        return False

"""
is one add or remove away

We iterate over both the shorter and longer strings.

If they are the same char, keep iterating.

If they are not the same char but the same index, then 
    increment the longer string idx by 1 so we can see if
    they start to match up again
    
    once we have the case where the chars are not equivalent and
    the indexes are not equal then we know we have already skipped 
    a character in the longer string and they are 2 or more characters 
    different - return False

"""


def is_one_add_remove_away(shorter, longer):
    idx_s = 0
    idx_l = 0
    while idx_s < len(shorter) and idx_l < len(longer):
        if shorter[idx_s] == longer[idx_l]:
            # incr. the idx and compare the next chars
            idx_s += 1
            idx_l += 1
        else:
            if idx_s == idx_l:
                # incr. the idx of the longer string
                idx_l += 1
            else:
                # we are at diff idxs and have already checked the next so we are more than 1 off, return False
                return False
    return True






s1 =  'pale'
s2 = 'pae'
print(is_one_edit_away(s1, s2))