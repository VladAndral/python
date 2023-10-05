import numpy as np

def inputPosIntCheck(numInput):
    try:
        numInput = int(numInput)
        if numInput < 1:
            raise Exception
        else:
            return True
    except:
        print("Input should be an integer greater than zero, try again")
        return False

def inputNumCheck(numInput):
    try:
        numInput = float(numInput)
        return True
    except:
        print("Input should be a number, try again")
        return False


inputGood=False
while inputGood == False:
    print("How many rows in the matrix?")
    rowAmount=input("-->")
    inputGood=inputPosIntCheck(rowAmount)

rowAmount=int(rowAmount)

inputGood=False
while inputGood == False:
    print("How many columns in the matrix?")
    columnAmount=input("-->")
    inputGood=inputPosIntCheck(columnAmount)

columnAmount=int(columnAmount)

matrix = np.zeros((rowAmount, columnAmount))


for i in range(rowAmount):
    for j in range(columnAmount):
        inputGood=False
        while inputGood == False:
            element = input("Item for row {0} column {1}: ".format(i+1, j+1))
            inputGood=inputNumCheck(element)
        matrix[i,j] = element
        
def rowReduceMatrix(matrix):
    rowReduceMatrixRecursiveEForm(matrix, 0)

def rowReduceMatrixRecursiveEForm(matrix:np.ndarray, depth:int): # Don't have to return array
    
    if depth == columnAmount-1:
        return
    else:
        matrix[depth] = matrix[depth]/matrix[depth, depth]
        for i in range(depth+1, rowAmount):
            startNum:float = matrix[i,depth]
            if startNum < 0:
                matrix[i] = matrix[i]+(matrix[depth]*startNum)
            else:
                matrix[i] = matrix[i]-(matrix[depth]*startNum)
                
    rowReduceMatrixRecursiveEForm(matrix, depth+1)

def reduceEchelonForm(matrix):
    return 4


rowReduceMatrix(matrix)
print(matrix)
