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
    dic_vector_result = {index: value for index, value in enumerate(vector_result)}

    # ordenando em ordem crescente e cria uma lista contendo apenas as chaves
    dic_vector_result = sorted(dic_vector_result, key=dic_vector_result.get)

    print(vector_result)
    print(dic_vector_result)

    print(create_new_mutated_matrix(population, dic_vector_result))

def create_new_mutated_matrix(matrix, key_list):

    new_poppulation = []

    for i in range(0,10):
        new_poppulation.append(matrix[key_list[i]])

    line_list = [10, 9, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    father = []
    mother = []

    for i in range(0,5):
        father.append(new_poppulation[random.choice(line_list)])

    for i in range(0,5):
        mother.append(new_poppulation[random.choice(line_list)])

    do_mutation(father, mother)

    return new_poppulation

def do_mutation(father, mother):
    # TODO: Implementar método que faz mutação

# Inicio do programa
if __name__ == '__main__':
    matrix = createRandomMatrix()
    __fitness(matrix)