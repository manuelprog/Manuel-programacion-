def transpose(matrix):
    if matrix == None or len(matrix) == 0:
        return []
        
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
   
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
        return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

array = [
    [1,2,3],
    [5,6,7],
    [10,11,12]]

result = transpose(array)
print_matrix(result)

i = [
    [1,2,3],
    [5,6,7],
    [10,11,12]]
print(type(i))



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
    
    i = [
    [1,2,3],
    [5,6,7],
    [10,11,12]]
print(type(i))
    




