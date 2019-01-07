
"""String Rotation.

Assume you have a method is_substring() which checks if one word is a substring of another.
Given 2 substrings, s1 and s2, write code to check if s2 is a rotation of s1 using only 1
call to is_substring() (e.g., "waterbottle" is a rotation of "erbottlewat").

"""


'''

Discussion:

s1 = waterbottle = xy

x = wat
y = erbottle


s2 = erbottlewat = yx

if we concat the orig string together with itself twice we get

xyxy = waterbottlewaterbottle

this way we can now check to see if s2 is a rotation of s1 using substring

a few rules apply, since we are checking to determine if s2 is a rotation of s1

both strings need to be of equal length and len(str) > 0

'''

def is_substring(candidate_sub_string, string):
    is_sub = False
    if candidate_sub_string in string:
        is_sub = True
    return is_sub

def is_rotation(str1, str2):

    # fail-fast checks:
    #   1) both strings MUST BE equal length
    #   since a rotation necessarily must be the same length
    #   of the original array
    #   2) lengths of each string must be > 0
    lens1 = len(str1)

    if lens1 == len(str2) and lens1 > 0:
        s1s1 = str1 + str1

        if is_substring(str2, s1s1):
            return True

    else:
        return False


s1 = 'waterbottle'
s2 = 'erbottlewat'

print(is_rotation(s1, s2))



