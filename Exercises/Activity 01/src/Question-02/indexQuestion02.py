import matplotlib.pyplot as plt
import numpy as np
import random
 
environment =[]

# Cria a sala e o aspirador de pó, de 0.5 segundos ele atualiza com o novo estado da sala e do aspirador
def exibir(matriz):
    plt.imshow(matriz, 'gray')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.5)
    plt.clf()

# Recebe um int como parâmetro, utilizado para saber em que direção o aspirador deve andar
def agente_Objetivo(percepcao,):
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
 
# Cria a sala randomicamente com os pontos limpos e sujos
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

# Percorre a matriz da sala e guarda os pontos que estão sujos
def scan_environment(matrix):
    size = len(matrix[0])
 
    for x in range(size):
        for j in range(size):
            if matrix[x][j] == 2:
                environment.append([x, j])
 
if __name__ == '__main__':
 
    currLine = 1
    currCol = 1
 
    matriz = create_random_matriz(6)

    # Mapeamento utilizado para saber em que direção andar na sala
                 #x,j,d
    mapeamento = [[1, 1, 3],
                  [1, 2, 3],
                  [1, 3, 3],
                  [1, 4, 4],
                  [2, 4, 4],
                  [3, 4, 4],
                  [4, 4, 5],
                  [4, 3, 6],
                  [3, 3, 6],
                  [2, 3, 5],
                  [2, 2, 4],
                  [3, 2, 4],
                  [4, 2, 5],
                  [4, 1, 6],
                  [3, 1, 6],
                  [2, 1, 6]]
 
    i = 0  
    scan_environment(matriz)  
    rodando = True        
    pontos = 0
    # Compara cada posiciçao do mapeamento com o estado do aspirador, quando a posição do aspirador corresponde
    # a uma posição do mapeamento ele obtem sua "percepção" para saber se tem que limpar ou andar para a proxima direção
    # a cada posição que o aspirador andar ele e ganha um ponto, o objetivo é terminar com o menor número de pontos
    # quando o robo identifica que limpou a sala toda ele para sua execução
    while rodando:
        if (currCol == 1 and currLine == 1):
            i = 0
        if (mapeamento[i][0] == currCol and mapeamento[i][1] == currLine):
            if [currLine,currCol] in environment:
                matriz[currLine][currCol] = 0
                environment.remove([currLine,currCol])
                print('Limpou a sujeira')
                pontos += 1
                print("Pontos: " + str(pontos))
            else:
                print(agente_Objetivo(mapeamento[i][2]))
                pontos += 1
                print("Pontos: " + str(pontos))
                i += 1
            exibir(matriz)
        if (len(environment) == 0):
            rodando = False