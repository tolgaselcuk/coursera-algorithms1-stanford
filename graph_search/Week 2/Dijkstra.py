
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
    print "-------\nchoose shortest edge\ne:%s" %e
    new_e = []
    for i in e:
        print "i:%s,%s,%s" % i
        value = i[2] + X[i[0]][0]
        new_e.append((i[0],i[1],value))
    new_e.sort(key=getKey)
    print "chosen:%s\n-------" % (new_e[0],)
    return new_e[0]

def shorttest_path(g, s):
    X = {}

    X[s] = [0,'']
    print "X:%s" % X
    print "len_X:%s, len_g:%s" % (len(X), len(g))

    while len(X) <> len(g):
        edges = [g[k] for k in X]
        edges2 = [x for t in edges for x in t]
        print "edges2:%s" % edges2
        remove_list = []
        for e in edges2:
            print "e:%s" % (e,)
            if X.has_key(e[1]):
                remove_list.append(e)
        print "remove list:%s" % remove_list
        if len(remove_list):
            #edges2.remove(remove_list)
            edges2 = [x for x in edges2 if x not in remove_list]
        print "edges2:%s" % edges2
        shortest = choose_shortest_edge(X,edges2)
        print "shortest:%s" % (shortest,)
        X[shortest[1]] = [shortest[2], X[shortest[0]][1] + shortest[1]]
        print "X:%s" % X

    return X


#d = load_graph_into_dict("./dijkstraData.txt")
d = load_graph_into_dict("./testdata1.txt")
print d, len(d)
print "\n\n"

shorttest_path(d,'1')

#q=[('1', '2', 1), ('1', '8', 2), ('2', '1', 1), ('2', '3', 1)]
#r = [('1', '2', 1), ('2', '1', 1)]

#print [x for x in q if x not in r]
#q.remove(r)
#print q