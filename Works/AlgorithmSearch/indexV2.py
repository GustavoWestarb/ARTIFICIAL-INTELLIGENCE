import random
import math
import sys
from collections import namedtuple

# Cria uma linha aleatoria que vai de 0 a 20
def create_random_line(x=1, y=21 , z=20):
    change_seed()
    return random.sample(range(x, y), z)


# Cria uma matriz aleatoria de 20 por 20
def create_random_matriz():
    matrix = []
    for i in range(20):
        matrix.append(create_random_line())

    return(matrix)


def change_seed():
    pass


def real_random(x, y):
    change_seed()
    return random.randint(x, y)


def _fitness(population):
    for line in population:
        if len(line) == 20:
            line.append(line[0])

    rand_x = create_random_line(0, 100, len(population))
    rand_y = create_random_line(0, 100, len(population))

    dist_city_column = []
    for i in range(len(rand_x)):
        dist_city_line = []

        for j in range(len(rand_y)):
            d = pow((rand_x[i]-rand_x[j]) / 100, 2)
            e = pow((rand_y[i]-rand_y[j]) / 100, 2)
            dist_city_line.append(math.sqrt(d + e))

        dist_city_column.append(dist_city_line)

    vector_result = []
    for i, row in enumerate(population):
        count_sum = 0
        for j in range(len(population)):
            count_sum += dist_city_column[i][j]

        vector_result.append(count_sum)

    # adicionando o vector em um dictionary com a somas...
    dic_vector_result = {index: value for index, value in enumerate(vector_result)}

    # ordenando em ordem crescente e cria uma lista contendo apenas as chaves
    dic_vector_result = sorted(dic_vector_result, key=dic_vector_result.get)

    new_population = []
    # Percorre e seleciona todos os cromossomos escolhidos
    for idx in dic_vector_result:
        without_last = list(population[idx])

        #Retiro o último elemento do cromossomo para nao entrar em loop, pois foi adicionado igual ao primeiro
        without_last.pop()
        new_population.append(without_last)

    #print(create_new_mutated_matrix(population, dic_vector_result))
    new_population = create_new_mutated_matrix(new_population, dic_vector_result)

    return new_population


#Comeca o processo de mutacao
def create_new_mutated_matrix(matrix, key_list):

    new_poppulation = matrix[:10]

    #Roleta
    line_list = [9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    father = []
    mother = []

    father_indexs = []

    for i in range(0, 5):
        indx_choice = random.choice(line_list)
        father_indexs.append(indx_choice)
        father.append(new_poppulation[indx_choice])

    for i in range(0, 5):
        indx_choice = random.choice(line_list)
        while father_indexs.__contains__(indx_choice):
            indx_choice = random.choice(line_list)
        mother.append(new_poppulation[indx_choice])

    print('############################################## Matriz original ##############################################')
    print(matrix)

    print('############################################## Pais e maes antes da mutacao ##############################################')
    print(father)
    print(mother)

    Retorno = do_mutation_cycle(father, mother)

    new_poppulation = append_in_new_poppulation(Retorno.son, new_poppulation)
    new_poppulation = append_in_new_poppulation(Retorno.daughter, new_poppulation)

    return new_poppulation

def append_in_new_poppulation(to_append, population):
    for item in to_append:
        population.append(item)

    return population

def invert_random_column(father, mother):
    random_item_chromosome = real_random(0, 19)
    for i in range(len(father)):
        father_value = father[i][random_item_chromosome]
        father[i][random_item_chromosome] = mother[i][random_item_chromosome]
        mother[i][random_item_chromosome] = father_value

        Retorno = vanish_repeated_value(random_item_chromosome, i, mother, father)

        father = Retorno.mother
        mother = Retorno.father


    Retorno = namedtuple('retorno', 'father mother')
    Retorno.mother = mother
    Retorno.father = father

    return Retorno

def vanish_repeated_value(random_item_chromosome, i, mother, father):
    repetido = False
    for j in range(len(father[i])):
        if j != random_item_chromosome and father[i][j] == father[i][random_item_chromosome]:
            repetido = True
            father_value = father[i][j]
            father[i][j] = mother[i][j]
            mother[i][j] = father_value

            vanish_repeated_value(j, i, mother, father)

            break

    Retorno = namedtuple('retorno', 'mother father')
    Retorno.father = father
    Retorno.mother = mother

    return Retorno




def create_controll(matriz, clear_unique_values=True):
    controll = dict()
    for x, line in enumerate(matriz):
        for y, value in enumerate(line):
            key = f'{x}|{value}'
            if not controll.get(key):
                controll[key] = []
            controll[key].append(y)

    if clear_unique_values:
        for k, v in dict(controll).items():
            if len(v) == 1:
                controll.pop(k)

    return controll


def invert_repeted_values(m_1, m_2, first):
    controll = create_controll(m_1)

    for k, v in controll.items():
        x, value = [int(_) for _ in k.split('|')]

        if first:
            del v[0]
        for y in v:
            m_2_value = m_2[x][y]
            m_2[x][y] = value
            m_1[x][y] = m_2_value

    Retorno = namedtuple('retorno', 'father, mother')
    Retorno.father = m_1
    Retorno.mother = m_2

    print('passou')
    return Retorno


def do_mutation_cycle(father, mother):
    Retorno = invert_random_column(father, mother)
    # controll = create_controll(father)

    father = Retorno.father
    mother = Retorno.mother

    # first = True
    # while len(controll) > 0:
    #     Retorno = invert_repeted_values(father, mother, first)
    #     father = Retorno.father
    #     mother = Retorno.mother
    #     first = False
    #     controll = create_controll(father)

    print(' ############################################## Pai e Maes  ##############################################')

    print(father)
    print(mother)
    #controll = create_controll(father)

    Retorno = namedtuple('retorno', 'son daughter')
    Retorno.son = father
    Retorno.daughter = mother

    return Retorno


if __name__ == '__main__':

    matrix = create_random_matriz()
    for i in range(10000):
        matrix = _fitness(matrix)

    print('############################################## A matrix continua igual ?  ##############################################')
    print(matrix)
