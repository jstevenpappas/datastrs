




def gcd(gn, ln):

    if gn % ln == 0:
        return ln
    else:
        return gcd(ln, gn % ln)





'''

Recursive alg to use remainder to close in on greatest common denominator indicated by when modding the two numbers
    repeatedly is 0.

'''





#print(gcd(16, 12))

print(gcd(39, 2))