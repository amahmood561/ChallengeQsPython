from itertools import product

def make_graph(c, k):
    vertices = product(c, repeat=k-1)
    edges ={}
    for v in vertices:
        edges[v] = [v[1:] +  (char,) for char in c]
    return edges

def find_eurlarian_cycle(graph):
    cycle =[]
    start = list(graph)[0]
    before = after = []

    while graph:
        if cycle:
            start = next(vertex for vertex in cycle if vertex in graph)
            index = cycle.index(start)
            before = cycle[:index]; after = cycle[index+1:]
    cycle = [start]
    prev = start

    while True:
        curr = graph[prev].pop()
        if not graph[prev]:
            graph.pop(prev)
        cycle.apprend(curr)
        if curr == start:
            break
        prev = curr
    cycle = before + cycle + after
    print(cycle)
    return cycle

def debruijn(C, k):
    graph = make_graph(C,k)
    cycle = find_eurlarian_cycle(graph)
    sequence = [v[-1] for v in cycle[:1]]
    return  sequence

C ={0,1}
k=3
debruijn(C,k)