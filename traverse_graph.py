class GraphNode:

    def __init__(self, label, connections = []):
        self.label = label
        self.connections = connections.copy()
        for c in self.connections:
            c.connect(self)

    def connect(self, *nodes):
        for node in nodes:
            if not node in self.connections:
                self.connections.append(node)
                node.connect(self)

    def find(self, label):
        if self.label == label:
            return self
        else:
            for c in self.connections:
                return c.find(label)

    def __str__(self):
        return "<" + str(self.label) + " : " + ",".join(c.label for c in self.connections) + ">"

    def DFS(self, visited = list()):
        visited.append(self.label)
        DFS_tree = GraphNode(self.label)
        for c in sorted(self.connections, key = lambda x: ord(x.label)):
            if not c.label in visited:
                DFS_tree.connections.append(c.DFS(visited))
        return DFS_tree

    def BFS(self):
        BFS_tree =  GraphNode(self.label)
        added = {self.label : BFS_tree} # Dictionary to access Nodes -> Inefficiency of data structure
        scan_list = [self]

        while scan_list:
            node = scan_list.pop(0)
            for c in sorted(node.connections, key = lambda x: ord(x.label)):
                if not c.label in added:
                    scan_list.append(c)
                    new_node = GraphNode(c.label)
                    added[node.label].connections.append(new_node)
                    added[c.label] = new_node

        return BFS_tree


def tree_string(node, depth = 1) -> str:

    string_value = "< Node '" + str(node.label) + "'"

    if node.connections:
        string_value += "\n"
        for c in node.connections:
            string_value += "\t"*depth + tree_string(c, depth + 1) + "\n"

    string_value += ">"

    return string_value


'''
a = GraphNode("a")
b = GraphNode("b")
c = GraphNode("c")
d = GraphNode("d")
e = GraphNode("e")
f = GraphNode("f")
g = GraphNode("g")
h = GraphNode("h")

a.connect(b,g)
b.connect(c,g)
c.connect(d,e,h)
e.connect(f)
h.connect(c,f)
f.connect(e,h,g)
g.connect(a,b,f)

print("DFS TREE:")
print(tree_string(a.DFS()))

print("BFS TREE:")
print(tree_string(a.BFS()))
#print(a.BFS())
'''


'''
a = GraphNode("a")
b = GraphNode("b")
c = GraphNode("c")
d = GraphNode("d")
e = GraphNode("e")
f = GraphNode("f")

a.connect(e,b,f)
b.connect(e,a,f)
e.connect(a,b)
f.connect(a,b,c,d)
c.connect(f,d)
d.connect(f,c)

a_DFS = a.DFS()
print(tree_string(a_DFS))
'''

'''
a = GraphNode("a")
b = GraphNode("b")
c = GraphNode("c")
d = GraphNode("d")
e = GraphNode("e")
f = GraphNode("f")

a.connect(e,f,b)
e.connect(a,b)
b.connect(e,a,f)
f.connect(a,b)
c.connect(f,d)
d.connect(f,c)

print(tree_string(a.BFS()))
'''