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

def DFS_topological_order(g, s, f, current_label, visited=None, route=None):

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
            visited, route, f, current_label = DFS_topological_order(g, k[1], f, current_label, visited,route)
    f[s] = current_label
    current_label = current_label - 1
    return visited, route, f, current_label

def DFS_Loop(g, current_label = None):
    #init nodes and mark all unexplored
    nodes = g.keys()
    explored = dict(zip(nodes,[0 for i in nodes]))
    f = dict(zip(nodes,[0 for i in nodes]))

    #init the current label as max
    if current_label == None:
        current_label = len(nodes)

    #traverse all vertices
    for v in nodes:
        if not explored[v]:
            explored, route, f, current_label = DFS_topological_order(g,v,f,current_label,explored)

    return f, current_label

# d = load_graph_into_dict("./smallGraph2.txt")
# start_vertex = d.keys()[0]
# connected, route = DFS(d, start_vertex)
# print "connected", connected, "\n"
# print "route", route, "\n---------\n"
#
# d = load_graph_into_dict("./smallGraph2Labels.txt")
# start_vertex = d.keys()[0]
# connected_rec, route_rec = DFS_recursive(d, start_vertex)
# print "connected", connected_rec, "\n"
# print "recursive route", route_rec, "\n---------\n"
#
# d = load_graph_into_dict("./directedWithLabels.txt")
# start_vertex = d.keys()[0]
# connected_rec, route_rec = DFS_recursive(d, start_vertex)
# print "connected", connected_rec, "\n"
# print "recursive route", route_rec, "\n---------\n"

d = load_graph_into_dict("./directedWithLabels.txt")
print DFS_Loop(d)