import numpy as np

from numpy import array, linalg
m =([
    [1 , 2,-1],
    [2 , 0, 2],
    [-1, 1, 1,]])
matriz = ([
    [1 , 2,-1],
    [2 , 0, 2],
    [-1, 1, 1,]])
m=matriz

matriz = array([
    [1 , 2,-1],
    [2 , 0, 2],
    [-1, 1, 1,]])

vector=array([-8,13,8,-1])

# solución  lineal
solucion = linalg.solve(matriz, vector)

print('La solución es: ')
for i in range(0, len(solucion)):
    print(f'x{i}:', solucion[i])

bool = int=True
bool = complex, float, list= False
#enteros (int)
numberint= 2
print(numberint)


#decimales (float)
numberfloat = 2.5
print(numberfloat)

#complejos(complex)
numbercomplex =3+2j
print(numbercomplex)

A= matriz

int(str(A))

print[int(A)]

bool = int=True
bool = complex, float, list= False
print("str")
