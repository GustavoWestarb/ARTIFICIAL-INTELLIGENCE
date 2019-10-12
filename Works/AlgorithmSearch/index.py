import random
import math
import operator


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

    vector_result = []

    print(vector_result)

    for i, row in enumerate(population):
        countSum = 0
        for j, column in enumerate(population[0]):
            if(j+1 <= 19):
                countSum += dist_city_column[i][j+1]# + dist_city_column[i][j+1])
        
        vector_result.append(countSum)

    # adicionando o vector em um dictionary com a somas...
    #dic_vector_result = [(index, value) for index, value in enumerate(vector_result)]
    dic_vector_result = {index: value for index, value in enumerate(vector_result)}

    # ordenando em ordem crescente o valores das somas...
    #dic_vector_result = sorted(dic_vector_result, key=lambda x: x[1])
    dic_vector_result = sorted(dic_vector_result, key=dic_vector_result.get)

    print(vector_result)
    print(dic_vector_result)

    print(swap_matrix_row(population, dic_vector_result))

#Método que ordena a matrix da população conforme a lista de aptidão.
def swap_matrix_row(matrix, key_list):
    resting_line = []
    for i in range(len(matrix)):
        resting_line = matrix[i]
        matrix[i] = matrix[key_list[i]]
        matrix[key_list[i]] = resting_line

    return matrix

# Inicio do programa
if __name__ == '__main__':
    matrix = createRandomMatrix()
    __fitness(matrix)