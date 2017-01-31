def load_file_into_list(f):
    data = [int(line.strip()) for line in open(f, 'r')]
    return data

def count_split_inversions(r, s):
    # inputs : two sorted arrays
    # counts the split inversions between the two arrays
    # while merging them, keeping sorted
    # returns: the number of total split inversions and a new merged&sorted array

    len_r = len(r)
    len_s = len(s)
    max_len = len_r + len_s
    #print "%d %d %d" % (len_r,len_s, max_len)
    #print r, s

    i = j = 0
    t = []
    num_split_inversions = 0

    for k in range(max_len):
        if i == len_r:
            #print "adding rest of s=%s" % s[j:]
            t.extend(s[j:])
            return num_split_inversions,t
        if j == len_s:
            #print "adding rest of r=%s" % r[i:]
            t.extend(r[i:])
            return num_split_inversions,t
        #print "k=%d r[%d]=%d s[%d]=%d" % (k, i, r[i], j, s[j])
        if r[i] <= s[j]:
            t.append(r[i])
            i +=1
        else:
            t.append(s[j])
            num_split_inversions += (len_r - i)
            #print "s[%s]=%s i smaller then %s. So %d more inversion(s)" % (j,s[j],r[i:],num_split_inversions)
            j += 1

    return num_split_inversions, t


def count_inversions(r):
    # inputs : an array of numbers
    # counts the number of inversions
    # returns: the total number of inversions and the sorted version of the array

    n = len(r)
    h = n // 2

    # base case : if len(r) is 1, then return the array itself
    if n == 1:
        print "array of len 1 is already sorted: %s" % r
        return 0, r

    print "\n-------\nSorting array %s of length %d" % (r,n)

    num_of_left_inversions, left = count_inversions(r[:h])
    num_of_right_inversions, right = count_inversions(r[h:])

    print "\nMerging two sorted arrays %s and %s" % (left,right)

    num_of_split_inversions, result = count_split_inversions(left, right)

    total_num_of_inversions = num_of_left_inversions + num_of_right_inversions + num_of_split_inversions

    return total_num_of_inversions, result


#print merge([1,3,5,7],[2,4,6,8])
#print merge([2,4,6,8],[1,3,5,7])
#print merge([2,3,4,5],[1,6,7,8])
#print merge([1,2,3,4],[5,6,7,8])

#print "\n=====\nNumber of inversions : %d. The sorted array is : %s" % count_inversions([5, 4, 7, 8, 2, 3, 6, 1, 9])
#print "\n=====\nNumber of inversions : %d. The sorted array is : %s" % count_inversions([5])
#print "\n=====\nNumber of inversions : %d. The sorted array is : %s" % count_inversions([5,5])


lst = load_file_into_list("./IntegerArray.txt")
print len(lst), lst

print "\n=====\nNumber of inversions : %d. The sorted array is : %s" % count_inversions(lst)
