
def load_graph_into_dict(f):
    data = [line.strip().split("\t") for line in open(f, 'r')]

    d = {}
    for k in data:
        vertice = head = k[0]
        tails = k[1:]
        tails2 = [t.split(',') for t in tails]
        len_tails = len(tails)
        heads = [head for i in range(len_tails)]
        edges = zip(heads,[t[0] for t in tails2],[t[1] for t in tails2])
        d[vertice] = edges
    return d


#d = load_graph_into_dict("./dijkstraData.txt")
d = load_graph_into_dict("./testdata1.txt")
print "\n\n"
print d
