
from collections import defaultdict

"""
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
case insert/remove:
    1 string would need to be 1 char less than the other to be eligible

case replace:
    both strings need to be same size

'''


def is_one_edit_away(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    # replace
    if len1 == len2:
        '''
        iterate over a string, comparing each char, track the count of inequal chars
        ... at end of iterate... if only chars found diff 1 time, replace is true
        else false
        '''
        return is_one_edit_replace(str1, str2)
    else:
        # pass in shortest str fisrt to avoid index out of bounds
        if ((len1+1) == len2):

            return is_one_add_remove_away(str1, str2)
        elif ((len1-1) == len2):

            return is_one_add_remove_away(str2, str1)



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


def is_one_add_remove_away(shorter, longer):
    idx_s = 0
    idx_l = 0
    while idx_s < len(shorter) and idx_l < len(longer):
        print('comparing {s} and {l}'.format(s=shorter[idx_s], l=longer[idx_l]))
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
        '''
        if shorter[idx_s] != longer[idx_l]:
            if (idx_s != idx_l):
                return False
            else:
                idx_l += 1
        else:
            idx_s += 1
            idx_l += 1
        '''
    return True






s1 =  'pale'
s2 = 'pae'
print(is_one_edit_away(s1, s2))