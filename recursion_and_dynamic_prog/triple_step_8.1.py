

"""Triple Step.

A child running up a flight of stairs with n steps can either hop 1, 2 or 3 steps at a time.


"""


def count_ways(n):
    if n < 1:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

print(count_ways(10))