"""
    Check Permutation
        Given 2 strings, write a method to decide if 1 is a permutation of the other.
        E.g., 'abcd' is permutation of 'dcba'

    Lessons here:
        1) Don't leave out obvious short-circuit case (lengths!= equal in this case...)!
        2) Modified version of hash table used here in form of char_array to hold char frequency
        3) instead of creating some crazy permutation method, we were just able to sort the strings - simple, cleaner.

"""

class CheckPermutation(object):


    def __init__(self):
        pass


    def str_to_sorted_list(self, string):
        str_list = [(char) for char in string]
        str_list.sort()
        return str_list

    '''
        a permutation of one string 
            1) must have same characters, though in diff order
            2) must be of same length 
    '''
    def is_permutation(self, string1, string2):

        if (len(string1) != len(string2)):
            return False

        list_str1 = self.str_to_sorted_list(string1)
        list_str2 = self.str_to_sorted_list(string2)

        return (list_str1 == list_str2)


    def is_permutation_char_cnt(self, string1, string2):

        # short circuit return for unequal lenghts
        if (len(string1) != len(string2)):
            return False

        # build the array to hold all the ASCII chars
        char_arr = [0] * 128

        for c1 in string1:
            # get frequency for each char
            char_arr[ord(c1)] += 1


        for c2 in string2:
            # for second string, to see if it matches in char frequency, decrement the array for this char
            #  if it's zero then there is a difference
            char_arr[ord(c2)] -= 1

            if (char_arr[ord(c2)] < 0):
                return False

        return True



def main():

    cp = CheckPermutation()

    str1 = 'abcd'
    str2 = 'abdc'

    no_perm = 'wxyz'

    print('Are {str1} and {str2} permutations of each other?: {val}'.format(str1=str1, str2=str2,
                                                                            val=cp.is_permutation(str1, str2)))
    print('Are {str1} and {str2} permutations of each other?: {val}'.format(str1=str1, str2=no_perm,
                                                                            val=cp.is_permutation(str1, no_perm)))

    print('\nNow, methods use char_array to hold frequency of each character...\n')

    print('Are {str1} and {str2} permutations of each other?: {val}'.format(str1=str1, str2=str2,
                                                                            val=cp.is_permutation_char_cnt(str1, str2)))
    print('Are {str1} and {str2} permutations of each other?: {val}'.format(str1=str1, str2=no_perm,
                                                                            val=cp.is_permutation_char_cnt(str1, no_perm)))





if __name__ == "__main__":
    main()