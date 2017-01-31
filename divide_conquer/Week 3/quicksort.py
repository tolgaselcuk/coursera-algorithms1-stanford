global rec_count1
global rec_count2
global rec_count3

def load_file_into_list(f):
    data = [int(line.strip()) for line in open(f, 'r')]
    return data

def choose_pivot_first(lst,left,right):
    # inputs a list
    # and returns the first element as the pivot element for partitioning
    return lst[left]

def choose_pivot_last(lst,left,right):
    # inputs a list
    # and returns the last element as the pivot element for partitioning
    # and swaps the last element with first
    tmp = lst[right-1]
    lst[right-1] = lst[left]
    lst[left] = tmp

    return lst[left]

def choose_pivot_median(lst,left,right):
    # inputs a list
    # and returns the element in the middle between the first, last and the middle elements of the array

    first = (lst[left], left)
    last = (lst[right-1], right-1)
    middle = (lst[ (left+right-1) // 2], (left+right-1) // 2)

    #print first, last, middle

    srtd = [first,last,middle]
    srtd.sort()

    #swap the first and the median srtd[1][0]

    tmp = lst[srtd[1][1]]
    lst[srtd[1][1]] = lst[left]
    lst[left] = tmp

    #print tmp, lst[left], lst[srtd[1][1]]

    return srtd[1][0]


def partition_array_easy(lst,left,right):
    # inputs an array
    # partitions it around a chosen pivot
    # using extra memory
    # and returns a partitioned array around element pvt

    pvt = choose_pivot_first(lst,left,right)

    less = []
    greater = []
    for i in range(left+1, right+1):
        #print i, left + i
        if lst[i] > pvt:
            greater.append(lst[i])
        elif lst[i] < pvt:
            less.append(lst[i])

    result = less
    result.append(pvt)
    result += greater

    return result

def partition_array_inplace(lst,left,right):
    # inputs an array
    # partitions it around a chosen pivot in place, with no extra memory
    # and returns a partitioned array around element pvt

    pvt = choose_pivot_first(lst,left,right)

    i = left + 1
    for j in range(left+1,right):
        if lst[j] < pvt:
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp
            i += 1
    lst[left] = lst[i-1]
    lst[i-1] = pvt

    print i, j

    return lst

def quicksort_with_first(lst,left,right):

    global rec_count1
    if left == right:
        right += 1
    print "-------"
    print "quicksorting array %s from %d to %d : %s" % (lst, left ,right, lst[left:right])
    rec_count1 += right - left - 1
    print rec_count1

    if right-left < 2 :
        print "    ....exiting without recursing"
        return

    pvt = choose_pivot_first(lst,left,right)
    print "pvt : %d" % pvt

    i = left + 1
    for j in range(left + 1, right):
        if lst[j] < pvt:
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp
            i += 1
    lst[left] = lst[i - 1]
    lst[i - 1] = pvt

    print "i : %d, lst : %s" % (i, lst)

    quicksort_with_first(lst,left, i-1)
    quicksort_with_first(lst, i, right)

def quicksort_with_last(lst,left,right):

    global rec_count2
    if left == right:
        right += 1
    print "-------"
    print "quicksorting array %s from %d to %d : %s" % (lst, left ,right, lst[left:right])
    rec_count2 += right - left - 1
    print rec_count2

    if right-left < 2 :
        print "    ....exiting without recursing"
        return

    pvt = choose_pivot_last(lst,left,right)
    print "pvt : %d" % pvt

    i = left + 1
    for j in range(left + 1, right):
        if lst[j] < pvt:
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp
            i += 1
    lst[left] = lst[i - 1]
    lst[i - 1] = pvt

    print "i : %d, lst : %s" % (i, lst)

    quicksort_with_last(lst,left, i-1)
    quicksort_with_last(lst, i, right)

def quicksort_with_median(lst,left,right):

    global rec_count3
    if left == right:
        right += 1
    print "-------"
    print "quicksorting array %s from %d to %d : %s" % (lst, left ,right, lst[left:right])
    rec_count3 += right - left - 1
    print rec_count3

    if right-left < 2 :
        print "    ....exiting without recursing"
        return

    pvt = choose_pivot_median(lst,left,right)
    print "pvt : %d" % pvt

    i = left + 1
    for j in range(left + 1, right):
        if lst[j] < pvt:
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp
            i += 1
    lst[left] = lst[i - 1]
    lst[i - 1] = pvt

    print "i : %d, lst : %s" % (i, lst)

    quicksort_with_median(lst,left, i-1)
    quicksort_with_median(lst, i, right)


lst = load_file_into_list("./QuickSort.txt")
print len(lst), lst

arr = [3,8,2,5,1,4,7,6]
rec_count1 = 0
rec_count2 = 0
rec_count3 = 0

#print choose_pivot_first(arr,0,len(arr))
#print choose_pivot_last(arr,0,len(arr))
#print choose_pivot_median(arr,0,len(arr))

#print partition_array_easy(arr,0,len(arr)-1)
#print partition_array_inplace(arr,0,len(arr)-1)

#quicksort(arr,0,len(arr))
#quicksort_with_first(lst,0,len(lst))
#quicksort_with_last(lst,0,len(lst))
quicksort_with_median(lst,0,len(lst))
