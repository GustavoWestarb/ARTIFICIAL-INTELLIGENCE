import random
import math


rand_x = random.sample(range(0, 100), 20)
rand_y = random.sample(range(0, 100), 20)

# Cria uma matriz aleatoria de 20 por 20
def createRandomMatrix():
    matrix = []
    for i in range(20):
        matrix.append(createRandomLine())

    return(matrix)

# Cria uma linha aleatoria que vai de 0 a 20
def createRandomLine():
    return random.sample(range(1, 21), 20)


def __fitness(population):

    print(population)

    for line in population:
        line.append(line[0])

    dist_city_column = []
    
    for i in range(len(rand_x)):
        dist_city_line = []

        for j in range(len(rand_y)):
            
            #print(rand_x[i])
            d = pow((rand_x[i]-rand_x[j]) / 100, 2)
            e = pow((rand_y[i]-rand_y[j]) / 100, 2)
            dist_city_line.append(math.sqrt(d + e))
        

        dist_city_column.append(dist_city_line)

    print(dist_city_column)

    vectorResult = []

    print(vectorResult)

    for i, row in enumerate(population):
        countSum = 0
        for j, column in enumerate(population[0]):
            if(j+1 <= 19):
                countSum += dist_city_column[i][j+1]# + dist_city_column[i][j+1])
        
        vectorResult.append(countSum)

    # adicionando o vector em um dictionary com a somas...
    dic_vectorResult = [(index, value) for index, value in enumerate(vectorResult)]

    # ordenando em ordem crescente o valores das somas...
    dic_vectorResult = sorted(dic_vectorResult, key=lambda x: x[1])

    print(vectorResult)
    print(dic_vectorResult)

# Inicio do programa
if __name__ == '__main__':
    matrix = createRandomMatrix()
    __fitness(matrix)