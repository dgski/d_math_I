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



def print_mat(m: list):
    for i in m:
        print(i)

def col(m: list, i: int) -> list:
    return [row[i] for row in m]

def cols(m:list) -> list:
    return [col(m,i) for i in range(len(m[0]))]

def multiply_mat(m1: list,m2:list) -> list:
    new = []
    for i in m1:
        new_row = []
        for j in cols(m2):
            new_row.append(dot_product(i,j))
        new.append(list(new_row))
        new_row.clear()
    return new

def dot_product(l1,l2):
    result = 0
    for i,j in zip(l1,l2):
        result += i * j
    return result

def matrix_power(m: list,i: int) -> list:
    last = m.copy()
    for i in range(2,i + 1):
        last = multiply_mat(last,m)
    return last

def bin_add(i: int,j: int) -> int:
    return 1 if (i != 0 or j != 0) else 0

def bin_add_mat(m1: list, m2: list):
    new = []
    for row_of_1,row_of_2 in zip(m1,m2):
        new_row = []
        for i,j in zip(row_of_1, row_of_2):
            new_row.append(bin_add(i,j))
        new.append(list(new_row))
        new_row.clear()
    return new


def rel_matrix_plus(m:list) -> list:
    last = m
    for i in range(2,len(m) + 1):
        last = bin_add_mat(last, matrix_power(m,i))
    return last

    

'''
J = [[0,1,0,0],
     [0,0,1,0],
     [0,0,0,1],
     [0,1,0,0]]

print("G^1")
print_mat(J)
print("")
print("G^2")
print_mat(matrix_power(J,2))
print("")
print("G^3")
print_mat(matrix_power(J,3))
print("")
print("G^4")
print_mat(matrix_power(J,4))
print("")
print("G^+")
print_mat(rel_matrix_plus(J))
'''

G = [[0,0,0,0,0,1],
     [1,0,0,0,0,0],
     [0,1,0,1,0,0],
     [0,0,1,0,1,0],
     [0,0,0,0,1,1],
     [0,1,0,0,0,0]]

G_power2 = matrix_power(G,2)
print_mat(G_power2)


def is_partial_order(m):
    return is_transitive(m) and is_antisymmetric(m) and is_reflexive(m) 