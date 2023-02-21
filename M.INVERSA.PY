# datos

A = [[1,5,2],[0,1,4],[1,8,1]]
m = len(A)
n = len(A[0])

m1 = m-1
n2 = n*2

if m != n:
    print("Error: La matriz no es cuadrada. Por tanto, no es invertible.")

else:
    
    #  matriz identidad
    
    I = []
    for i in range(m):
        I.append([])
        for j in range(n):
            if i == j:
                I[i].append(1)
            else:
                I[i].append(0)
        
        # Matriz (A|I)
        
        A[i]+=I[i]
    
    for i in range(m):
        print(A[i])
    print("")

    # Triangularización superior

    for j in range(n):
        
        # Búsqueda de pivote
        
        l = [i for i in range(m) if A[i][j] !=0 and i>=j]
        if len(l) == 0:
            print("Error: La matriz no es invertible.")
        else:
            j0 = l[0]
            a = A[j]
            b = A[j0]
            A[j] = b
            A[j0] = a

            # Triangularización superior

            for i in [i for i in range(j+1,m) if A[i][j] != 0]:
                alpha = -A[i][j]/A[j][j]
                for k in range(n2):
                    A[i][k] += A[j][k]*alpha
                       
    for i in range(m):
        print(A[i])
    print("")

    # Triangularización inferior

    for j in range(1,m):
        for i in range(m1):
            alpha = -A[i][j]/A[j][j]
            for k in range(i+1,n2):
                A[i][k] += A[j][k]*alpha

    for i in range(m):
        print(A[i])
    print("")

    # Transformación a la matriz identidad

    for i in range(m):
        for j in range(n2):
            A[i][j] /= A[i][i]

    for i in range(m):
        print(A[i])
    print("")


class Data:
    id = 0
    
    def __init__(self, i):
        self.id = i
 
    def __int__(self):
        return self.id
    
    def __init__(self, i):
        self.id = i
 
    def __float__(self):
        return self.id
    
    def __init__(self, i):
        self.id = i
 
    def __complex__(self):
        return self.id
    int= m
    print("int(m)")

