from queue import Queue

DEBUG_MODE = False

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
    dist = dict(zip(nodes,[99999 for i in nodes]))
    dist[s] = 0

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
                dist[k[1]] = dist[v] + 1
                q.enqueue(k[1])
                if DEBUG_MODE: print "%s enqueued" % k[1]

            else:
                if DEBUG_MODE: print "%s already explored." % k[1]
        if DEBUG_MODE: print "queue : %s" % q
        if DEBUG_MODE: print "explored : %s" % explored

    return explored, dist

def CC_BFS(g):
    # finds connected components of an undirectional graph
    nodes = g.keys()
    visited = dict(zip(nodes, [0 for i in nodes]))
    print nodes, "\n\n", visited, "\n\n"
    connected_components = []
    for n in nodes:
        print "n :%s, visited[%s]:%s" % (n, n, visited[n])
        if not visited[n]:
            visited[n] = 1
            print "visited : %s" % visited
            cc = BFS(g,n)[0]
            print "cc : %s" % cc
            for i in cc.keys():
                if cc[i]: visited[i] = 1
            #connected_components.append(cc)
            connected_components.append([i[0] for i in cc.items() if i[1]>0])
    return connected_components


#d = load_graph_into_dict("./smallGraph.txt")

# start_vertex = d.keys()[0]
# connected, distance = BFS(d, start_vertex )
# print connected, distance, "\n"

d = load_graph_into_dict("./UnconnectedGraph.txt")
print "CC : %s" % CC_BFS(d)