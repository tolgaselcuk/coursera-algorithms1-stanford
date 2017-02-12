DEBUG_MODE = False

def load_graph_into_dict(f):
    data = [line.strip().split("\t") for line in open(f, 'r')]

    d = {}
    for k in data:
        vertice = head = k[0]
        tails = k[1:]
        tails2 = [t.split(',') for t in tails]
        len_tails = len(tails)
        heads = [head for i in range(len_tails)]
        edges = zip(heads,[t[0] for t in tails2],[int(t[1]) for t in tails2])
        d[vertice] = edges
    return d

def getKey(item):
    return item[2]

def choose_shortest_edge(X, e):
    if DEBUG_MODE: print "-------\nchoose shortest edge\ne:%s" %e
    new_e = []
    for i in e:
        if DEBUG_MODE: print "i:%s,%s,%s" % i
        value = i[2] + X[i[0]][0]
        new_e.append((i[0],i[1],value))
    new_e.sort(key=getKey)
    if DEBUG_MODE: print "chosen:%s\n-------" % (new_e[0],)
    return new_e[0]

def shorttest_path(g, s):
    X = {}

    X[s] = [0,'']
    if DEBUG_MODE: print "X:%s" % X
    if DEBUG_MODE: print "len_X:%s, len_g:%s" % (len(X), len(g))

    while len(X) <> len(g):
        if DEBUG_MODE: print "====Run===="
        edges = [g[k] for k in X]
        edges2 = [x for t in edges for x in t]
        if DEBUG_MODE: print "edges2:%s" % edges2
        remove_list = []
        for e in edges2:
            if DEBUG_MODE: print "e:%s" % (e,)
            if X.has_key(e[1]):
                remove_list.append(e)
        if DEBUG_MODE: print "remove list:%s" % remove_list
        if len(remove_list):
            edges2 = [x for x in edges2 if x not in remove_list]
        if DEBUG_MODE: print "edges2:%s" % edges2
        shortest = choose_shortest_edge(X,edges2)
        if DEBUG_MODE: print "shortest:%s" % (shortest,)
        X[shortest[1]] = [shortest[2], X[shortest[0]][1] +shortest[1] + ', ']
        if DEBUG_MODE: print "X:%s" % X

    return X


d = load_graph_into_dict("./dijkstraData.txt")
#d = load_graph_into_dict("./testdata2.txt")
#print d, len(d)
print "\n\n"

paths = shorttest_path(d,'1')
print paths

for i in (7,37,59,82,99,115,133,165,188,197):
    if paths.has_key(str(i)):
        print "%s," % paths[str(i)][0]
    else:
        print '1000000'

#q=[('1', '2', 1), ('1', '8', 2), ('2', '1', 1), ('2', '3', 1)]
#r = [('1', '2', 1), ('2', '1', 1)]

#print [x for x in q if x not in r]
#q.remove(r)
#print q