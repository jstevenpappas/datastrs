

def fib_r(n):
    if n <= 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
nn=7
#print('fib series for {s}: {sum}'.format(s=nn, sum=fib_r(nn)))






def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


# Dynamic programming
# top-down
def fib_memo(n):
    memo = [0 for i in range(n + 1)]
    return fibonacci_td(n, memo)

def fibonacci_td(n, memo):
    if n == 1 or n == 0:
        return n
    if memo[n] == 0:
        memo[n] = fibonacci_td(n-1, memo) + fibonacci_td(n-2, memo)
    return memo[n]

n=998
#print(fib(n))
print(fib_memo(n))



# bottom-up

def fib_bu(n):

    if n == 0:
        return 0

    num = 0
    num_following = 1

    for i in range(2, n):
        sum = num + num_following

        num = num_following
        num_following = sum

    return num + num_following

n = 100000
#print('bottom up programming', fib_bu(n))
#print(fib_bu(n))