def merge(r,s):
    # inputs : two sorted arrays
    # merges them keeping sorted
    # returns: a new merged&sorted array

    len_r = len(r)
    len_s = len(s)
    max_len = len_r + len_s
    print "%d %d %d" % (len_r,len_s, max_len)
    print r, s

    i = j = 0
    t = []
    for k in range(max_len):
        if i == len_r:
            print "adding rest of s=%s" % s[j:]
            t.extend(s[j:])
            return t
        if j == len_s:
            print "adding rest of r=%s" % r[i:]
            t.extend(r[i:])
            return t
        print "k=%d r[%d]=%d s[%d]=%d" % (k, i, r[i], j, s[j])
        if r[i] < s[j]:
            t.append(r[i])
            i +=1
        else:
            t.append(s[j])
            j += 1
    return t


def mergesort(r):
    # inputs : an array of numbers
    # returns: the sorted version of it in a new array

    n = len(r)
    h = n // 2

    # base case : if len(r) is 1, then return the array itself
    if n == 1:
        print "array of len 1 is already sorted: %s" % r
        return r

    print "Sorting array %s of length %d" % (r,n)

    left = mergesort(r[:h])
    right = mergesort(r[h:])

    print "Merging two sorted arrays %s and %s" % (left,right)

    result = merge(left,right)

    return result


#print merge([1,3,5,7],[2,4,6,8])
#print merge([2,4,6,8],[1,3,5,7])
#print merge([2,3,4,5],[1,6,7,8])
#print merge([1,2,3,4],[5,6,7,8])

#print mergesort([5,4,7,8,2,3,6,1,9])
#print mergesort([5])
#print mergesort([5,4])

print mergesort([5,3,8,9,1,7,0,2,6,4])
