
class TreeNode:
    '''Node that belongs to tree data structure'''
    def __init__(self,value, children = []):
        self.value = value
        self.children = children
        self.parent = None

        if not self.children:
            for c in children:
                c.setparent(self)

    def addparent(self, node):
        self.parent = node

    def __str__(self) -> str:

        string_value = "< TreeNode '" + str(self.value) + "'"

        if self.children:
            string_value += "\n"
            for c in self.children:
                string_value += "\t" + str(c) + "\n"

        string_value += ">"

        return string_value


    def preOrderTraverse(self, func):
        '''Vertex is visited before it's decendants'''
        func(self)
        for c in self.children:
            c.preOrderTraverse(func)

    def postOrderTraverse(self, func):
        '''Vertex is visted after it's decendants'''
        for c in self.children:
            c.postOrderTraverse(func)
        func(self)

    def leafcount(self): 
        if not self.children:
            return 1
        else:
            return sum(i.leafcount() for i in self.children)

    def is_root(self):
        return True if self.parent else False
            

a = TreeNode("The solar system",
                [TreeNode("Inner Solar System",
                    [TreeNode("Inner planets"), TreeNode("Asteroid Belt")]),
                TreeNode("Outer Solar System",
                    [TreeNode("Outer planets"), TreeNode("Centaurs")])])

print(a)

a.preOrderTraverse(lambda x: print(x.value))
print("")
a.postOrderTraverse(lambda x: print(x.value))

print("Leaf count:" + str(a.leafcount()))
print("Root?: " + str(a.is_root()))


# Post Order = f,i,h,e,b,g,c,a,d
# Pre Order = d,f,b,i,h,e,a,c,g