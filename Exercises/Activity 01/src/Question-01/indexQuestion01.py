import matplotlib.pyplot as plt
import numpy as np
import random
 
def exibir(matriz):
    plt.imshow(matriz, 'gray')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.5)
    plt.clf()
 
def agente_reativo_simples(percepcao,):
    global currLine
    global currCol
    if percepcao == 3:
        currLine += 1
        return 'abaixo'
    elif percepcao == 4:
        currCol += 1
        return 'direita'
    elif percepcao == 5:
        currLine -= 1
        return 'acima'
    elif percepcao == 6:
        currCol -= 1
        return 'esquerda'
 
def create_random_matriz(size):
    size = size
    matrix = np.full((size, size), 0)
 
    for x in range(size):
        for j in range(size):
            if x == 0 or x == (size - 1):
                matrix[x][j] = 1
            elif j == 0 or j == (size - 1):
                matrix[x][j] = 1
            else:
                random_status = random.randint(0, 1)
                if random_status == 0:
                    matrix[x][j] = 0
                else:
                    matrix[x][j] = 2
    return matrix
 
if __name__ == '__main__':
 
    currLine = 1
    currCol = 1
 
    matriz = create_random_matriz(6)
                 #x,y,d
    mapeamento = [[1, 1, 3],
                  [1, 2, 3],
                  [1, 3, 3],
                  [1, 4, 4],
                  [2, 4, 4],
                  [3, 4, 4],
                  [4, 4, 5],
                  [4, 3, 6],
                  [3, 3, 6],
                  [2, 3, 6],
                  [1, 3, 5],
                  [1, 2, 4],
                  [2, 2, 4],
                  [3, 2, 4],
                  [4, 2, 5],
                  [4, 1, 6],
                  [3, 1, 6],
                  [2, 1, 6]]
 
    i = 0              
    while True:
        if (currCol == 1 and currLine == 1):
            i = 0
        if (mapeamento[i][0] == currCol and mapeamento[i][1] == currLine):
            if matriz[currLine][currCol] == 2:
                matriz[currLine][currCol] = 0
                print('Limpou a sujeira')
            else:
                print(agente_reativo_simples(mapeamento[i][2]))
                i += 1
            exibir(matriz)