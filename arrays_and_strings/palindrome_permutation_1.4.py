from collections import defaultdict

"""
    Permutation of Palindrome

    Given a string, check if it is a permutation of a palindrome.
        Input:      Tactcoa or Tact Coa
        Output:     True(permutations: "taco cat", "atco cta", etc)


    The solution below checks whether the string 'could' be a palindrom - it doesn't check if it is 
    in palindrome form (i.e., same spelled backards as forwards)... but only that it meets the 
    requirements of such.
    
    Palindrom - a word spelled the same backwards as forwards.

        Facts:  1) palindromes can be of odd and even len
                2) 
                    a) if string is odd len:
                        -> it must have 1 char that had odd freq and the rest of the chars of even freq
                    b) if string is even:
                        -> all chars must have even freq


"""


def is_perm_of_palindrome(input):
    # format the input
    input = ''.join(input.split())
    # get input string len to see if it is odd or even
    input_len = len(input)
    # build a dict of chars with their frequency/counts in the input string
    char_freq_dict = defaultdict(int)
    for char in input:
        char_freq_dict[char] += 1
    #
    # even case
    if input_len % 2 == 0:
        for char, freq in char_freq_dict.items():
            if freq % 2 != 0:
                return False
    else:
        # odd case
        # strings w/ odd len must have exactly one char with odd freq
        # so iterate over the frequencies in the dict and ensure there is
        # only 1 where the count is exactly 1!
        chars_odd_freq = []
        for char, freq in char_freq_dict.items():
            if freq % 2 != 0:
                chars_odd_freq.append(char)
        if len(chars_odd_freq) != 1:
            return False
    return True


class PalindromePermutation(object):

    def __init__(self):
        pass

    '''
    inputs w/ even char count:
        strings w/ even len must consist of chars w/ even freq

    inputs w/ odd char count
        strings w/ odd len must have EXACTLY 1 char w/ odd freq
    
    '''
    def is_perm_of_palindrome(self, input):
        # format the input
        input = ''.join(input.split())
        # get input string len to see if it is odd or even
        input_len = len(input)
        # build a dict of chars with their frequency/counts in the input string
        char_freq_dict = defaultdict(int)
        for char in input:
            char_freq_dict[char] += 1
        #
        # even case
        if input_len % 2 == 0:
            for char, freq in char_freq_dict.items():
                if freq % 2 != 0:
                    return False
        else:
            # odd case
            # strings w/ odd len must have exactly one char with odd freq
            # so iterate over the frequencies in the dict and ensure there is
            # only 1 where the count is exactly 1!
            chars_odd_freq = []
            for char, freq in char_freq_dict.items():
                if freq % 2 != 0:
                    chars_odd_freq.append(char)
            if len(chars_odd_freq) != 1:
                return False
        return True

def main():

    pp = PalindromePermutation()

    palin_perm = 'rad ar '
    print('is "{input}" a perm of a palindrome?: {is_perm}'.format(input=palin_perm, is_perm=pp.is_perm_of_palindrome(palin_perm)))

    non_palin_perm = 'rad arr '
    print('is "{input}" a perm of a palindrome?: {is_perm}'.format(input=non_palin_perm,
                                                                   is_perm=pp.is_perm_of_palindrome(non_palin_perm)))


if __name__ == "__main__":
    main()