import random

DEBUG_MODE = False

def load_graph_into_list(f):
    data = [line.strip().split("\t") for line in open(f, 'r')]
    vertices = [data[x][0] for x in range(len(data))]

    if DEBUG_MODE: print "vertices: %s" % vertices
    if DEBUG_MODE: print "--------\n"
    all_edges = []
    for k in data:
        #if DEBUG_MODE: print k
        head = k[0]
        tails = k[1:]
        len_tails = len(tails)
        heads = [head for i in range(len_tails)]

        #if DEBUG_MODE: print heads
        #if DEBUG_MODE: print tails

        edges = zip(heads,tails)
        all_edges.extend(edges)

        #if DEBUG_MODE: print len(edges), edges
        #if DEBUG_MODE: print "-------\n"
    return vertices, all_edges

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

def pick_edge(e):
    r = random.randint(0,len(e)-1)
    return e[r]

def find_pairs_in_list(e):
    for k in range(len(e)-1):
        #print e[k]
        head = e[k][0]
        tail = e[k][1]
        #print head, tail
        found = False
        for x in range(len(e)):
            #print "comparing %s and %s" % (e[k], e[x])
            if e[x] == tuple([str(tail), str(head)]):
                print ".......found! %s = %s" % (e[k], e[x])
                found = True
        if found == False:
            print "******** not found!!!!! *****"

def find_minCut_from_dict(org_d,trials=1):

    min_cut = 99999999
    for y in range(1,trials+1):
        #init d, v
        d = org_d.copy()
        v = d.keys()

        while len(v) > 2:
            # init list of edges to choose from and pick one
            e = [x for t in d.values() for x in t]
            edge = pick_edge(e)
            if DEBUG_MODE: print "edge (%s,%s) is selected" % edge

            vertex_to_remove = edge[0]
            vertex_to_contract = edge[1]
            if DEBUG_MODE: print "removing vertex %s, contracting to %s" % (vertex_to_remove, vertex_to_contract)

            # find incident nodes
            incident_nodes = list(set([t[1] for t in d[vertex_to_remove]]))
            if DEBUG_MODE: print "incident list : %s" % incident_nodes

            # change vertex_to_remove <--- vertex_to_contract in edges in incident nodes
            for i in incident_nodes:
                lst = d[i]
                if DEBUG_MODE: print "org list : %s" % lst
                new = []
                for l in lst:
                    if l[1] == vertex_to_remove:
                        if l[0] != vertex_to_contract:
                            new.append((l[0],vertex_to_contract))
                    else:
                        new.append(l)
                if DEBUG_MODE: print "new list: %s " % new
                d[i] = new

            # add edges in vertex_to_remove to corresponding nodes
            lst = d[vertex_to_remove]
            for l in lst:
                new = (vertex_to_contract, l[1])
                if new[0] != new[1]:
                    if DEBUG_MODE: print "adding (%s, %s)" % new
                    d[vertex_to_contract] = d[vertex_to_contract]+ [(new[0], new[1])]

            # delete the node to be removed
            del d[vertex_to_remove]
            if DEBUG_MODE: print "new graph is : %s" % d

            # update the list of vertices for while loop
            v = d.keys()

        new_min_cut = len([x for t in d.values() for x in t]) / 2
        print "%d. %s" % (y, new_min_cut)

        if new_min_cut < min_cut:
            min_cut = new_min_cut
    print "the winner is : %s" % min_cut


def find_minCut(org_v,org_e,trials=1):

    min_cut = 99999999
    for y in range(1,trials+1):
        #init v,e
        v = list(org_v)
        e = list(org_e)

        #loop until 2 verteces left
        while len(v) > 2:
            edge = pick_edge(e)

            if DEBUG_MODE: print "edge (%s,%s) is selected" % edge

            vertex_to_remove = edge[0]
            vertex_to_contract = edge[1]
            if DEBUG_MODE: print "removing vertex %s, contracting to %s" % (vertex_to_remove, vertex_to_contract)
            v.remove(vertex_to_remove)

            if DEBUG_MODE: print "new vertex list is : %s" % v

            #replacing vertex_to_remove with vertex_to_contract
            remove_list = []
            for k in e:
                if k[0] == vertex_to_remove:
                    vertex_to_add = (vertex_to_contract,k[1])
                    remove_list.append(k)
                    if vertex_to_add[0] != vertex_to_add[1]: e.append(vertex_to_add)
                if k[1] == vertex_to_remove:
                    vertex_to_add = (k[0], vertex_to_contract)
                    remove_list.append(k)
                    if vertex_to_add[0] != vertex_to_add[1]: e.append(vertex_to_add)

            if DEBUG_MODE: print remove_list

            for k in remove_list:
                e.remove(k)

            if DEBUG_MODE: print "new edges list : %s" % e
            if DEBUG_MODE: print "------"

        new_min_cut = len(e)/2
        print y,". ", new_min_cut

        if new_min_cut < min_cut:
            min_cut = new_min_cut
    print "the winner is : %s" % min_cut

#d = load_graph_into_dict("./smallerMinCut.txt")
d = load_graph_into_dict("./kargerMinCut.txt")
find_minCut_from_dict(d,100)

#v, e = load_graph_into_list("./smallerMinCut.txt")
#v, e = load_graph_into_list("./kargerMinCut.txt")
#find_minCut(v,e,10)

