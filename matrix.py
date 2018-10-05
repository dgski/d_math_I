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
