"""
Is Unique:
    Implement and algorithm to determine if a string has all unique chars.

    What if you cannot use an additional datastructure?


    Solutions above:
        1) is_str_uniq()
            iteratively stores characters in a hash/dict{} and prechecks if the curr char
            exists as a key to the hash/dict (i.e., has been seen before)

        2) is_str_uniq_no_ext_ds()
            This uses no external datastructure.
            The method iterates the index of each char in the string and uses the idx to
            check if the curr char exists witihin string comprised of the characters before and after it.
            It uses list slices to build this string that excludes the curr char.

        3) is_str_uniq_char_arr()
            This method assumes a 128 char set (i.e., 7 bit ASCII characters).
            It builds a 'char_array' of 128 elements each set to False.
            For each character in the string, the ord assoc with that char is used to index into
            the char_array and set that element to True.
            If that array element is True, then this element has been seen before and False (not uniq) is returned.
            Else, the element in the array assoc to the char's ord value is set to True and the loop continues.


        4) is_str_uniq_bit()
            This uses several bit-shifting techniques.

            First, we keep a var 'bit_tracker' to represent the ord value of the curr char.
                a) We loop over each char in the string
                b) we test if the Nth bit is set in the 'bit_tracker' var by AND'ing it with '1 shifted ord(char)'
                    values to the left - this isolates the ord_val
                    E.g.,
                        bit_tracker with only ord('b') val of 98 stored
                        0b100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                        1 << ord('a') which is 1 shifted left 97
                        0b010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

aa                      0b110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
bb

                        0b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                        (above, AND'ing both yield 0 b/c no aligning bits in same place)


                        We test to see if the ord('a') val of 97 exists in the bit_tracker so we AND both
                            (if both 1 on top and bottom then 1, else 0)

                        ANDing both doesn't show 97 in bit_tracker so result is 0:
                            if bit_tracker & (1 << ord_val) > 0:
                                return False

                c) if above doesn't yield bits in same place (or result > 0), then we just append the ord val of the
                    char to bit_tracker for subsequent evaluations:
                        bit_tracker |= (1 << ord_val)

                    This is done appending 'bit_tracker' with its current value OR'd the 1 bit shifted ord(char) to the
                        left
                        (e.g., OR'ing so that if both 0 top/bottom then zero, otherwise 1)

                        0b100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                        0b010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                        -
                        0b110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

                e) the for loop repeats from step b and the method returns True if no ord_vals found in same position in
                    bit pattern

"""

class UniqString(object):

    def __init__(self):
        pass


    def is_str_uniq(self, input_string):
        is_uniq = True
        str_chars = dict()

        for s in input_string:
            if s in str_chars.keys():
                is_uniq = False
            str_chars.update({s: s})

        return is_uniq


    def is_str_uniq_no_ext_ds(self, string):
        is_uniq = True

        for idx in range(0, len(string)-1):
            search_val = string[idx]
            if idx < len(string)-1:
                if search_val in (string[:idx] + string[idx+1:]):
                    is_uniq = False

        return is_uniq


    def is_str_uniq_char_arr(self, string):
        char_set = [False] * 128
        for char in string:
            if char_set[ord(char)] is True:
                return False
            char_set[ord(char)] = True
        return True


    def is_str_uniq_bit(self, string):

        # set up var to hold bits specific to
        bit_tracker = 0

        for char in string:
            ord_val = ord(char)
            # Bit Hack #2.
            # Tests if the n-th bit is set
            if (bit_tracker & (1 << ord_val) > 0):

                return False

            # Bit Hack #3.
            # Sets the n-th bit.
            bit_tracker |= (1 << ord_val)
            print(bin(bit_tracker))

        return True


    def is_even_wout_division(self, x):
        # Bit Hack #1. Check if the integer is even or odd.
        # tests if least significant bit is odd (or 1)
        if ((x & 1) == 0):
            return True
        else:
            return False




def main():

    test_str_not_uniq = 'pappas'
    test_str_uniq = 'bacdef'
    us = UniqString()


    print("String is {nustr} - contains uniq chars? {val}".format(nustr=test_str_not_uniq,
                                                                  val=us.is_str_uniq(test_str_not_uniq)))

    print("String is {ustr} - contains uniq chars? {val}".format(ustr=test_str_uniq,
                                                                  val=us.is_str_uniq(test_str_uniq)))

    print("(no external datastructure) String is {nustr} - contains uniq chars? {val}".format(nustr=test_str_not_uniq,
                                                                  val=us.is_str_uniq_no_ext_ds(test_str_not_uniq)))

    print("(no external datastructure) String is {ustr} - contains uniq chars? {val}".format(ustr=test_str_uniq,
                                                                 val=us.is_str_uniq_no_ext_ds(test_str_uniq)))

    print("(array bools for each char) String is {nustr} - contains uniq chars? {val}".format(nustr=test_str_not_uniq,
                                                                  val=us.is_str_uniq_char_arr(test_str_not_uniq)))

    print("(array bools for each char) String is {ustr} - contains uniq chars? {val}".format(ustr=test_str_uniq,
                                                                 val=us.is_str_uniq_char_arr(test_str_uniq)))

    print("(bit vector) String is {nustr} - contains uniq chars? {val}".format(nustr=test_str_not_uniq,
                                                                                              val=us.is_str_uniq_bit(
                                                                                                  test_str_not_uniq)))

    print("(bit vector) String is {ustr} - contains uniq chars? {val}".format(ustr=test_str_uniq,
                                                                                             val=us.is_str_uniq_bit(
                                                                                                 test_str_uniq)))

    num_even = 8
    num_odd = 9
    print('is {num} even?: {val}'.format(num=num_even, val=us.is_even_wout_division(num_even)))

    print('is {num} even?: {val}'.format(num=num_odd, val=us.is_even_wout_division(num_odd)))



if __name__ == "__main__":
    main()