from stack import Stack

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

def DFS_recursive(g,s,visited=None, route=None):
    nodes = g.keys()
    if visited == None:
        visited = dict(zip(nodes, [0 for i in nodes]))
    if route == None:
        route = []

    visited[s] += 1
    if DEBUG_MODE: print "visited : %s" % visited

    route.append(s)
    if DEBUG_MODE: print "route : %s" % route

    for k in g[s]:
        if DEBUG_MODE: print "k : %s" % (k,)
        if not visited[k[1]]:
            visited, route = DFS_recursive(g,k[1],visited,route)
    return visited, route


def DFS(g,s):
    nodes = g.keys()
    #edges = [x for t in g.values() for x in t]
    visited = dict(zip(nodes,[0 for i in nodes]))
    route = []

    st = Stack()
    st.push(s)
    if DEBUG_MODE: print "%s pushed" % s

    if DEBUG_MODE: print "stack : %s" % st
    if DEBUG_MODE: print "explored : %s" % visited

    while not st.isEmpty():
        v = st.pop()
        route.append(v)
        visited[v] += 1

        print "route : %s" % route
        if DEBUG_MODE: print "%s popped" % v
        for k in g[v]:
            if DEBUG_MODE: print "%s selected" % (k,)
            if not visited[k[1]]:
                visited[k[1]] += 1
                st.push(k[1])
                if DEBUG_MODE: print "%s pushed" % k[1]
            else:
                if DEBUG_MODE: print "%s already explored." % k[1]
        if DEBUG_MODE: print "stack : %s" % st
        if DEBUG_MODE: print "explored : %s" % visited

    return visited, route


d = load_graph_into_dict("./smallGraph2.txt")
start_vertex = d.keys()[0]
connected, route = DFS(d, start_vertex)
print "connected", connected, "\n"
print "route", route, "\n---------\n"

d = load_graph_into_dict("./smallGraph2Labels.txt")
start_vertex = d.keys()[0]
connected_rec, route_rec = DFS_recursive(d, start_vertex)
print "connected", connected_rec, "\n"
print "recursive route", route_rec, "\n"
