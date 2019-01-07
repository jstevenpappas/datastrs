from linked_list_impl import LinkedList
import math
"""Sum Lists.
You have 2 numbers represented by a linked list, where each node contains a
single digit.  The digits are stored in reverse order, such that the 1's digit
is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked lisst.
E.g., 
Input: (7->1->6) + (5->9->2).  That is, 617 + 295
Output: 2->1->9.  That is, 912
"""

'''
    isolating digits of an integer
    
    1) get the number of digits in the integer:  len = int(math.log10(val)) + 1
    (get the log of the int and add 1 to it
    
    2) while i <= len:
        lsd = val % base 
        # append to some structure like an array
        val = val/base
        i = i + 1
'''
def isolate_lsd_to_list(val, base=10):
    # need the len of the val so we take the log and add 1
    val_len = int(math.log10(val)) + 1
    res_list = LinkedList()
    for i in range(val_len):
        lsd = (val % base)
        print(lsd)
        res_list.append(lsd)
        val /= 10
    return res_list


def list_sum(head, base=10):
    tot = 0
    exp = 0
    while head is not None:
        # first num* base^0 (or 1) second num *base^1 (or * base) third num * base^2
        tot += (head.data * (base ** exp))
        exp += 1
        head = head.next
    return tot


def sum_lists(first, second):
    first_digit = list_sum(first.head)
    second_digit = list_sum(second.head)
    sum = first_digit + second_digit
    print('sum of {f} + {s} = {v}'.format(f=first_digit, s=second_digit, v=sum))
    print('in the return list, we expect that the sum {v} is in reverse'.format(v=sum))
    sum_result = isolate_lsd_to_list(sum)
    return sum_result


print('contents of first list containing digit')
first_num = LinkedList()
first_num.append(7)
first_num.append(1)
first_num.append(6)
first_num.iterate()
print('contents of second list containing digit')
sec_num = LinkedList()
sec_num.append(5)
sec_num.append(9)
sec_num.append(2)
sec_num.iterate()


ret_val = (sum_lists(first_num, sec_num))
print('output of return list')
ret_val.iterate()

num = 789
print('isolate lsd to list')
ll = isolate_lsd_to_list(789)

while ll.head is not None:
    print(int(ll.head.data/1))
    ll.head = ll.head.next