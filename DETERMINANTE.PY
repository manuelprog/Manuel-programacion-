dEF determinante(MatrizX,ntotal=0):
if len(MatrizX)==1
valor=MatrizX[0][0]
return valor

    else
for j in range (len(MatrizX)):

    nMatriz=RecortarMatriz(MatrizX,0,j)
    op = MatrizX[0][j]
    op=MatrizX[0][j]*((-1)**(2+j))

    ntotal += op*determinante(nMatriz)
    return ntotal 
