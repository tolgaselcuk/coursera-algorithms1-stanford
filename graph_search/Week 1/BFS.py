from queue import Queue

DEBUG_MODE = True


def load_graph_into_dict(f):
    data = [line.strip().split("\t") for line in open(f, 'r')]

    d = {}
    for k in data:
        vertice = head = k[0]
        tails = k[1:]
        len_tails = len(tails)
        heads = [head for i in range(len_tails)]
        edges = zip(heads,tails)
        d[vertice] = edges
    return d

def BFS(g,s):
    nodes = g.keys()
    edges = [x for t in g.values() for x in t]
    explored = dict(zip(nodes,[0 for i in nodes]))
    #if DEBUG_MODE: print nodes, edges, explored

    q = Queue()
    q.enqueue(s)
    if DEBUG_MODE: print "%s enqueued" % s
    explored[s] += 1

    if DEBUG_MODE: print "queue : %s" % q
    if DEBUG_MODE: print "explored : %s" % explored

    while not q.isEmpty():
        v = q.dequeue()
        if DEBUG_MODE: print "%s dequeued" % s
        for k in g[v]:
            if DEBUG_MODE: print "%s selected" % (k,)
            if not explored[k[1]]:
                explored[k[1]] += 1
                q.enqueue(k[1])
                if DEBUG_MODE: print "%s enqueued" % k[1]

            else:
                if DEBUG_MODE: print "%s already explored." % k[1]
        if DEBUG_MODE: print "queue : %s" % q
        if DEBUG_MODE: print "explored : %s" % explored

    return explored


d = load_graph_into_dict("./smallGraph.txt")
print BFS(d, d.keys()[0])
