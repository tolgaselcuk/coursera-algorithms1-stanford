from stack import Stack

DEBUG_MODE = False

def load_graph_into_dict_multiline(f):
    data = [line.strip().split() for line in open(f, 'r')]
    d = {}
    for k in data:
        vertice = head = int(k[0])
        tail = int(k[1])
        edge = (head,tail)
        if d.has_key(vertice):
            d[vertice].append(edge)
        else:
            d[vertice] = [edge]
    return d

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

def reverse_graph(g):
    gnew = {}
    for n in g:
        for e in g[n]:
            v = (e[1], e[0])
            if gnew.has_key(e[1]):
                gnew[e[1]].append(v)
            else:
                gnew[e[1]] = [v]
    return gnew

def DFS(g, s, t, f, source, leaders, visited=None):
    # nodes = g.keys()
    # if visited == None:
    #     visited = dict(zip(nodes, [0 for i in nodes]))

    visited[s] += 1
    leaders[s] = source

    if DEBUG_MODE: print "visited : %s" % visited

    for k in g[s]:
        if DEBUG_MODE: print "k : %s" % (k,)
        if visited.has_key(k[1]) and not visited[k[1]]:
            visited, t, f, source, leaders = DFS(g, k[1], t, f, source, leaders, visited)
    t = t + 1
    f[s] = t
    if DEBUG_MODE: print "t:%s and f[s]:%s" % (t, f)
    return visited, t, f, source, leaders


def DFS_stack(g, s, t, f, source, leaders, visited=None):
    # nodes = g.keys()
    # if visited == None:
    #     visited = dict(zip(nodes, [0 for i in nodes]))

    st = Stack()
    st.push(s)

    while not st.isEmpty():
        v = st.pop()
        visited[v] += 1
        leaders[v] = source

        if DEBUG_MODE: print "visited : %s" % visited

        for k in g[v]:
            if DEBUG_MODE: print "k : %s" % (k,)
            if visited.has_key(k[1]) and not visited[k[1]]:
                st.push(k[1])
                #visited, t, f, source, leaders = DFS(g, k[1], t, f, source, leaders, visited)
        t = t + 1
        f[v] = t
        if DEBUG_MODE: print "t:%s and f[s]:%s" % (t, f)
    return visited, t, f, source, leaders

def DFS_Loop(g):
    #1st PASS : traverse all vertices with DFS on reversed graph,
    # assign order numbers f[i] that will be used in the 2nd pass

    #reverse the graph for the 1st pass
    grev = reverse_graph(g)
    #print len(grev)
    #print grev['861201']

    #init nodes and mark all unexplored
    nodes = grev.keys()
    nodes.sort(reverse=True)
    explored = dict(zip(nodes,[0 for i in nodes]))

    #init order and leaders lists
    t = 0
    f = dict(zip(nodes,[0 for i in nodes]))
    source = None
    leaders = dict(zip(nodes,[0 for i in nodes]))

    for i in nodes:
        print "i:%s" % i
        if DEBUG_MODE: print "node : %s" % i
        if DEBUG_MODE: print "explored : %s" % explored
        if not explored[i]:
            source = i
            explored, t, f, source, leaders = DFS_stack(grev, i, t, f, source, leaders, visited=explored)
        if DEBUG_MODE: print "---------\n"

    f_orders = f.copy()

    #2nd PASS : traverse all vertices with DFS, setting leaders to all nodes

    #use the original graph and change the node names with order numbers f[n]
    g_new = {}
    for k in reverse_graph(grev).keys():
        for v in g[k]:
            v_new = (f[k],f[v[1]])
            if g_new.has_key(f[k]):
                g_new[f[k]].append(v_new)
            else:
                g_new[f[k]] = [v_new]
    if DEBUG_MODE: print "g_new : %s" % g_new

    # init nodes and mark all unexplored
    nodes = g_new.keys()
    nodes.sort(reverse=True)
    explored = dict(zip(nodes, [0 for i in nodes]))

    #init leaders list
    t = 0
    f = dict(zip(nodes,[0 for i in nodes]))
    source = None
    leaders = dict(zip(nodes,[0 for i in nodes]))

    for i in nodes:
        if DEBUG_MODE: print "node : %s" % i
        if DEBUG_MODE: print "explored : %s" % explored
        if not explored[i]:
            source = i
            explored, t, f, source, leaders = DFS_stack(g_new, i, t, f, source, leaders, explored)
        if DEBUG_MODE: print "---------\n"

    return leaders, f_orders


g = load_graph_into_dict_multiline("./SCC_HW.txt")
#print g
#print g['861201']

ldr, order =  DFS_Loop(g)
print "ldr   :%s \norder :%s" % (ldr, order)

scc = {}
for d in ldr.keys():
    val = ldr[d]
    if scc.has_key(val):
        scc[val].append(d)
    else:
        scc[val] = [d]

print "scc : %s" % scc

srt = []
for s in scc.values():
    srt.append(len(s))

srt.sort(reverse=True)
print "srt:%s" % srt


