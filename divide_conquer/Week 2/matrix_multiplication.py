import random


def print_matrix(r):
    # type: (list) -> None
    # takes a matrix and prints it friendly, each row on a new line
    for i in range(len(r)):
        print r[i]
    return None



def generate_random_matrix(n):
    # inputs : integer dimension (n)
    # and generates an (n x n) matrix of integers (1 .. n)
    # outputs : the matrix as a list

    out = [[0 for x in range(n)] for y in range(n)]
    for x in range(n):
        for y in range(n):
            out[x][y] = random.randint(1, n)
    return out


def bruteforce_multiply(r, s):
    # inputs : two matrices of dimension both (nxn)
    # multiplies them using brute force : runtime O(n^3)
    # outputs : new matrix as a list

    n = len(r)

    out = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                out[i][j] += r[i][k] * s[k][j]
    return out


def add_matrices(A, B):
    # sums each element of same indices of two matrices
    # outputs a new matrix
    n = len(A)
    out = [[A[x][y] + B[x][y] for y in range(n)] for x in range(n)]
    return out


def substract_matrices(A, B):
    # substracts each corresponding element (A(i,j)-B(i,j)) of same indices of two matrices
    # outputs a new matrix
    n = len(A)
    out = [[A[x][y] - B[x][y] for y in range(n)] for x in range(n)]
    return out


def combine_matrices(A, B, C, D):
    # type: (list, list, list, list) -> list
    # input : 4 matrices of A,B,C and D in order
    # combines them into a new matrix :
    #  [ A  B
    #    C  D ]
    # output : the combined new matrix

    n = len(A)
    up = [A[x] + B[x] for x in range(n)]
    down = [C[x] + D[x] for x in range(n)]
    out = up + down
    #print "combined : \n", print_matrix(out)

    return out


def recursive_multiply(r, s):
    # type: (list, list) -> list
    n = len(r)
    if n == 2:
        return bruteforce_multiply(r, s)
    else:
        h = n // 2
        A = [r[x][:h] for x in range(h)]
        B = [r[x][h:] for x in range(h)]
        C = [r[h + x][:h] for x in range(h)]
        D = [r[h + x][h:] for x in range(h)]
        E = [s[x][:h] for x in range(h)]
        F = [s[x][h:] for x in range(h)]
        G = [s[h + x][:h] for x in range(h)]
        H = [s[h + x][h:] for x in range(h)]

        # print "A", print_matrix(A)
        # print "B", print_matrix(B)
        # print "C", print_matrix(C)
        # print "D", print_matrix(D)
        # print "E", print_matrix(E)
        # print "F" ,print_matrix(F)
        # print "G", print_matrix(G)
        # print "H", print_matrix(H)

        A_E = recursive_multiply(A, E)
        B_G = recursive_multiply(B, G)
        A_F = recursive_multiply(A, F)
        B_H = recursive_multiply(B, H)
        C_E = recursive_multiply(C, E)
        D_G = recursive_multiply(D, G)
        C_F = recursive_multiply(C, F)
        D_H = recursive_multiply(D, H)

        out = combine_matrices(add_matrices(A_E, B_G),
                               add_matrices(A_F, B_H),
                               add_matrices(C_E, D_G),
                               add_matrices(C_F, D_H)
                               )

        return out


def strassens_subcubic_multiply(r, s):
    # type: (list, list) -> list
    n = len(r)
    if n == 2:
        return bruteforce_multiply(r, s)
    else:
        h = n // 2
        A = [r[x][:h] for x in range(h)]
        B = [r[x][h:] for x in range(h)]
        C = [r[h + x][:h] for x in range(h)]
        D = [r[h + x][h:] for x in range(h)]
        E = [s[x][:h] for x in range(h)]
        F = [s[x][h:] for x in range(h)]
        G = [s[h + x][:h] for x in range(h)]
        H = [s[h + x][h:] for x in range(h)]

        # print "A", print_matrix(A)
        # print "B", print_matrix(B)
        # print "C", print_matrix(C)
        # print "D", print_matrix(D)
        # print "E", print_matrix(E)
        # print "F" ,print_matrix(F)
        # print "G", print_matrix(G)
        # print "H", print_matrix(H)

        P1 = strassens_subcubic_multiply(A, substract_matrices(F, H))
        P2 = strassens_subcubic_multiply(add_matrices(A, B), H)
        P3 = strassens_subcubic_multiply(add_matrices(C, D), E)
        P4 = strassens_subcubic_multiply(D, substract_matrices(G, E))
        P5 = strassens_subcubic_multiply(add_matrices(A, D), add_matrices(E, H))
        P6 = strassens_subcubic_multiply(substract_matrices(B, D), add_matrices(G, H))
        P7 = strassens_subcubic_multiply(substract_matrices(A, C), add_matrices(E, F))

        out = combine_matrices(add_matrices(substract_matrices(add_matrices(P5, P4),P2),P6),
                               add_matrices(P1, P2),
                               add_matrices(P3, P4),
                               substract_matrices(substract_matrices(add_matrices(P1, P5), P3), P7)
                               )

        return out


m = generate_random_matrix(32)
n = generate_random_matrix(32)

print "matrix 1 :"
print_matrix(m)
print "matrix 2 :"
print_matrix(n)

result1 = bruteforce_multiply(m, n)
print "result 1, by bruteforce"
print_matrix(result1)

result2 = recursive_multiply(m, n)
print "result 2, recursively multiply:"
print_matrix(result2)

result3 = strassens_subcubic_multiply(m, n)
print "result 3, Strassen's multiplication algorithm:"
print_matrix(result3)
