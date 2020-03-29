import numpy
import copy


def printn(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            print(round(n[i][j], 4), end=' ')
        print()



def dot(v1, v2):
    dp = 0
    for i in range(len(v1)):
        c = v1[i]*v2[i]
        dp = dp+c
    return dp


def smult(scalar, matrix):
    for i in range(len(matrix)):
        matrix[i] = scalar*matrix[i]
    return matrix


def projection(v1, v2):
    coeff = dot(v1, v2)/dot(v2, v2)
    projectv1onv2 = smult(coeff, v2)
    return projectv1onv2


def subtract(v1, v2):
    dif = []
    for i in range(len(v1)):
        dif.append(v1[i]-v2[i])
    return dif


def gramschmidt(x):
    v = [x[0]]
    for i in range(1, len(x)):
        c = x[i]
        for j in range(i):
            c = subtract(c, projection(x[i], v[j]))
        v.append(c)
    return v


def scale(x):
    v = gramschmidt(x)
    csum = []
    for i in range(len(v)):
        s = 0
        for j in range(len(v[i])):
            s = s + (v[i][j]**2)
        csum.append(s)
    # print(csum)
    for i in range(len(v)):
        for j in range(len(v[i])):
            v[i][j] = v[i][j]/(csum[i]**0.5)
    return v


def makeqandr(x):
    y = copy.deepcopy(x)
    y = numpy.transpose(y)
    temp = scale(x)
    q = numpy.transpose(temp)
    print("Q: ")
    printn(q)
    print()
    r = numpy.dot(temp, y)
    print("R: ")
    printn(r)
    print()

def printm(m):
    print("Matrix:")
    m = numpy.transpose(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()
    print()


test_case = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]]
#makeqandr(test_case)
mi = int(input("Number of rows: "))
ni = int(input("Number of columns: "))
matrix = []
for a in range(ni):
    ith = str(a + 1)
    x = [int(x) for x in input("Enter column " + ith + ": ").split()]
    matrix.append(x)
printm(matrix)
makeqandr(matrix)
