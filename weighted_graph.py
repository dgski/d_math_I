from traverse_graph import *

# Weighted Graph
class WGNode:

    def __init__(self, value):
        self.value = value
        self.connections = []

    def connect(self, *nodes):
        for node in nodes:
            if not node[1] in (c[1] for c in self.connections):
                self.connections.append((node[0],node[1],self))
                node[1].connect((node[0], self))

    def __str__(self) -> str:
        return "<" + str(self.value) + " : " + \
        ",".join("(" + str(c[0]) + "," + str(c[1].value) + ")" for c in self.connections) + ">"

    def MST(self):
        '''Use Prim's Algorithm to find the MST'''

        elgible = sorted(self.connections, key = lambda x: x[0])
        MST_root = GraphNode(self.value)
        added = {self.value : MST_root}

        for _ in range(self.size() - 1):

            current: tuple = elgible.pop(0)
            new_node = GraphNode(current[1].value)
            parent = added[current[2].value]
            parent.connections.append(new_node)
            added[current[1].value] = new_node

            elgible += (c for c in current[1].connections if c[1].value not in added)
            elgible.sort(key = lambda x: x[0])

        return MST_root


    def size(self, seen = list()):
        ''' Return the number of nodes '''
        seen.append(self.value)        
        if not self.connections:
            return 1

        return 1 + sum(c[1].size(seen) for c in self.connections if c[1].value not in seen)

a,b,c,d,e,f,g,h = WGNode("a"),WGNode("b"),WGNode("c"),WGNode("d"),WGNode("e"),WGNode("f"),WGNode("g"),WGNode("h")

a.connect((0,d),(9,f),(11,g))
d.connect((0,a),(8,f))
g.connect((11,a),(6,f),(1,h))
f.connect((9,a),(8,d),(6,g),(2,h),(3,e))
h.connect((1,g),(2,f),(7,b))
e.connect((10,a),(3,f),(5,c))
c.connect((5,e),(12,f),(4,b))
b.connect((4,c),(7,h))

a_MST = a.MST()
print(tree_string(a_MST))