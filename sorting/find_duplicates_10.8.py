"""Find Duplicates.

You have an array with all the numbers from 1 to N, where N is at most 32,000.
The array may have duplicate entries and you do not know what N is.
With only 4 kb of memory available, how do you print all the duplicate elements in the array.


"""
'''
so 2^15 = 32768 more than the num of ints need to represent all the ints (32000)

we create an array of 1000 elements - each holding up to 15 bits - more than enough to hold 
the value 32000


we iterate over the array, each time checking to see if it exists in our class

(in our class, we divide the int by 32 to get the element number, and mod the int 
to get its position in the bitvalue)

 

'''

class BitSet(object):
    def __init__(self, size):
        self.bitarr = [0 for i in range((size >> 5))] # div by 32 and create 1000 buckets


    # see if the int exists in its proper place
    def bget(self, pos):
        word_number = (pos >> 5) # div by 32
        bit_num = (pos % 32) # mod 32
        if (self.bitarr[word_number] & 1 << bit_num) != 0:
            print('wordnumber {w} bn {bn}'.format(w=word_number, bn=bit_num))
            print(bin(pos))
            print('true: {dupe}'.format(dupe=pos))
            return True
        else:
            False

    # set the int in the proper place
    def bset(self, pos):
        word_number = (pos >> 5)
        bit_num = (pos % 32)
        self.bitarr[word_number] |= 1 << bit_num


def check_dupes(arr):
    bs = BitSet(32000)
    arrlen = len(arr)
    for i in range(arrlen):
        num = arr[i]
        num0 = num -1 # b/c bitset starts at 0
        if bs.bget(num):
            return True #print(num)
        else:
            #return False
            #print('am i ever set?')
            bs.bset(num0)


arr = list()
for i in range(1, 32000):
    arr.append(i)

arr.append(31000)

check_dupes(arr)

print(len(arr))


