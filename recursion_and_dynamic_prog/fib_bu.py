
def fib_bu1(n):

    if n == 0:
        return 0

    num = 0
    num_following = 1

    for i in range(2, n):
        sum = num + num_following

        num = num_following
        num_following = sum

    return num + num_following




def fib_bu(n):

    if n==0:
        return n

    a = 0
    b = 1

    for i in range(2, n):

        c = a + b

        a = b
        b = c


    return a + b



n=5
print(fib_bu(n))