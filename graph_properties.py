# Properties of Directed Graphcs

test_graph_1 = {'A': ['A','B'],
                'B': ['B','C'],
                'C': ['C','A']}

test_graph_2 = {'E': ['A','B','C'],
                'A': ['C', 'B'],
                'B': ['C'],
                'C': [],
                'D': ['C']}

test_graph_3 = {'A':['E','B'],
                'B':['A','C'],
                'C':['B'],
                'D':[],
                'E':['A']}

def has_connection(graph, src, dst):
    return dst in graph[src]

def out_degree(graph,vertex):
    return len(graph[vertex])

def in_degree(graph,vertex):
    d = 0
    for v in graph:
        if vertex in v:
            d += 1
    return d


def is_reflexive(graph):
    for vertex,edges in graph.items():
        if vertex not in edges:
            return False
    return True

def is_antireflexive(graph):
    return not is_reflexive(graph)

def is_transitive(graph):
    for vertex_1,edges_1 in graph.items():
        for vertex_2 in edges_1:
            for vertex_3 in graph[vertex_2]:
                if not has_connection(graph, vertex_1, vertex_3):
                    return False
    return True

def is_symmetric(graph):
    for vertex, edges, in graph.items():
        for arrow in edges:
            if not has_connection(graph,arrow,vertex):
                return False
    return True

def is_antisymmetric(graph):
    return not is_symmetric(graph)

def walk(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for vertex in graph[start]:
        if vertex not in path:
            newpath = walk(graph, vertex, end, path)
            if newpath: return newpath



print("Testing Relexivity")
print(is_reflexive(test_graph_1))

print("Testing Transitivity")
print(is_transitive(test_graph_2))

print("Testing Symmetricity")
print(is_symmetric(test_graph_3))

print("Testing Walk")
print(walk(test_graph_1,'A','C'))