def karatsuba(x, y):
    # inputs : strings x and y of length of (n) both
    # multiplies them using a divide and conquer approach
    # returns the product as a string

    # input pre-processing
    # string sizes are made equal and even by filling by zeros on the left
    max_len = max(len(x), len(y))
    if max_len >1 and max_len % 2:
        max_len += 1
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    n = len(x)
    h = n//2
    print "===================================="
    print "Multiplying numbers x=%s, y=%s of length=%s" % (x, y, n)

    # handle base case
    # return x*y if strings of length = 1
    if n == 1:
        result = str(int(x) * int(y))
        print "result=", result
        print "-----------"
        return result

    b = x[h:]
    a = x[:h]
    d = y[h:]
    c = y[:h]
    print "a=%s b=%s c=%s d=%s" % (a,b,c,d,)

    ac = karatsuba(a, c)
    print "ac=%s" % ac

    bd = karatsuba(b, d)
    print "bd=%s" % bd

    a_b = str(int(a) + int(b))
    c_d = str(int(c) + int(d))
    abcd = karatsuba(a_b , c_d)

    print "abcd=%s" % abcd

    step1 = int(ac)
    step2 = int(bd)
    step3 = int(abcd) - step2 - step1
    print "step1=%s, step2=%s, step3=%s" % (step1,step2,step3)

    #result = str((step1 * (10 ** n)) + step2 + (step3 * (10 ** h)))
    result = str(int(str(step1) + (n * "0")) + step2 + int(str(step3) + (h * "0")))

    print "result=%s" % result
    print "-----------"
    return result

s1 = "3141592653589793238462643383279502884197169399375105820974944592"
s2 = "2718281828459045235360287471352662497757247093699959574966967627"
print karatsuba(s1,s2)

# import math
# n = 100000000
#
# print "e=", n ** 2
# print "a=", (n * n) * math.log(n)
# #print "d=", n ** (math.log(n))
# #print "b=", 2 ** n
#
# #print "c=", 2 ** (2 ** n)


