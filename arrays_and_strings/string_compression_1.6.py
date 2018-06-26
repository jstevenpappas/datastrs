"""


    String compression:
    
    Implement a method to perform basic string compression using the counts of the repeated characters.
    For example, the string aabcccccaaa would become a2b1c5a3.
    If the 'compressed' string would not become smaller than the original string, your method should return the 
    original string.
    
    You can assume the string only has upper and lowercase letters (a-z).

"""

def compress_string(string):
    char_cnt = 0
    comp_str = ''
    for idx in range(0, len(string)):
        # add a 1 for the current character
        char_cnt += 1

        # capture the char and its freq if we are beyond max index of string or consec chars don't match
        if idx +1 >= len(string) or string[idx] != string[idx+1]:
            comp_str += '{c}{f}'.format(c=string[idx], f=char_cnt)
            char_cnt = 0

    if len(comp_str) >= len(string):
        return string
    else:
        return comp_str


compressible = 'aabcccccaaa'
print(compress_string(compressible))

compression_not_worth_it = 'abc'
print(compress_string(compression_not_worth_it))

