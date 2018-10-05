from graph_properties import *

A = [1,2,3,4]
S = {(2,3),(1,4),(3,1)}
R = {(1,1),(2,1),(3,4),(4,2)}

def compose_rel(rel_x: set, rel_y: set) -> set:
    ''' x of y'''
    new = set()
    for i in rel_x:
        for j in rel_y:
            if i[0] == j[1]:
                new.add((j[0],i[1]))
    
    return new

def rel_power(vert_num: int, rel: set) -> set:

    if vert_num == 1:
        return rel

    last = rel
    for _ in range(vert_num - 1):
        last = compose_rel(rel,last)
    return last

def trans_closure_rel(vert_num: int, rel: set) -> set:

    last = rel

    for i in range(2,vert_num + 1):
        last = last.union(rel_power(i,rel))

    return last



#print(compose_rel(S,R))
#print(compose_rel(R,S))

R = {('d','a'),('a','b'),('b','c')}
S = {('a','a'),('b','d'),('b','c')}

print(compose_rel(S,R))
print(compose_rel(R,S))

S = {('a','b'),('a','c'),('c','d'),('c','a')}
R = {('b','c'),('c','b'),('a','d'),('d','b')}
'''
print(compose_rel(S,R))
# -> [(b,d),(b,a)]
print(compose_rel(R,S))
# -> [(a,c),(a,b),(c,b),(c,d)]
print(compose_rel(S,S))
# -> [(a,d),(c,c),(c,b),(c,c)]
print(compose_rel(R,R))
# -> [(b,b),(c,c),(a,b),(d,c)]
'''

G = {('a','d'),('d','a'),('b','a'),('c','b'),('c','d')}


#print(compose_rel(G,G))
#print(rel_power(3,G))
#print(trans_closure_rel(4,G))

G = {(1,2),(2,1),(1,4),(4,2),(3,4)}
#print(trans_closure_rel(4,G))





def is_partial_order(m):
    return is_transitive(m) and is_antisymmetric(m) and is_reflexive(m) 