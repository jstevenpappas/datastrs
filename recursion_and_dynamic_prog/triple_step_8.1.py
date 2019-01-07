

"""Triple Step.

A child running up a flight of stairs with n steps can either hop 1, 2 or 3 steps at a time.


"""


def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

print(count_ways(10))







def count_down(n):
    if n == 0:
        return 0
    tot = count_down(n-1) + 1
    return tot

print(count_down(100))





def cd(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return cd(n-1) + cd(n-2)

print(cd(10))