import random
import math
import sys
from collections import namedtuple
import os
import platform
import matplotlib.pyplot as plt


### Alunos que desenvolveram o trabalho Bruno G. Vigentas & Gustavo Westarb ###

MAX_ITERATIONS = 100
RATE_MUTATION = 0
POPULATION = 20
BEST_COST = 0


# Cria uma linha aleatoria que vai de 0 a 20
def create_random_line(x=1, y=21 , z=20):
    return random.sample(range(x, y), z)


# Cria uma matriz aleatoria de 20 por 20
def create_random_matriz():
    matrix = []
    for i in range(20):
        matrix.append(create_random_line())

    return(matrix)


#Cria um número randômico entre X e Y
def real_random(x, y):
    return random.randint(x, y)


#Executa a função de fitness
def _fitness(population):

    global BEST_COST

    #Adiciona o valor da primeira coluna para última, pois no problema do caxeiro viajante, deve sempre retornar para a cidade de partida
    population = _append_last_column(population)

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
    dic_vector_result_ordened = sorted(dic_vector_result, key=dic_vector_result.get)

    BEST_COST = dic_vector_result[dic_vector_result_ordened[0]]

    new_population = []
    # Percorre e seleciona todos os cromossomos escolhidos
    for idx in dic_vector_result_ordened:
        without_last = list(population[idx])

        #Retiro o último elemento do cromossomo para nao entrar em loop, pois foi adicionado igual ao primeiro
        without_last.pop()
        new_population.append(without_last)

    #print(create_new_mutated_matrix(population, dic_vector_result))
    new_population = create_new_mutated_matrix(new_population, dic_vector_result_ordened)

    return new_population


#Comeca o processo de crossover
def create_new_mutated_matrix(matrix, key_list):

    #Seleciona os 10 primeiros items da matriz, anteriormente ordenados como melhores
    new_poppulation = matrix[:10]

    #Roleta
    line_list = [9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    father = []
    mother = []

    father_indexs = []

    #Escolhe os 5 primeiros pais, baseado na chance de criada na roleta acima
    for i in range(0, 5):
        indx_choice = random.choice(line_list)
        father_indexs.append(indx_choice)
        father.append(new_poppulation[indx_choice])

    #Escolhe os outros 5 pais, baseado na chance de criada na roleta acima e ignorando os que já foram selecionados nos 5 primeiros pais
    for i in range(0, 5):
        indx_choice = random.choice(line_list)
        while father_indexs.__contains__(indx_choice):
            indx_choice = random.choice(line_list)
        mother.append(new_poppulation[indx_choice])

    _result_cycle = do_mutation_cycle(father, mother)

    new_poppulation = append_in_new_poppulation(_result_cycle.son, new_poppulation)
    new_poppulation = append_in_new_poppulation(_result_cycle.daughter, new_poppulation)

    return new_poppulation

#Adiciona os filhos a matriz principal
def append_in_new_poppulation(to_append, population):
    for item in to_append:
        population.append(item)

    return population

#Inverte aleatóriamente uma coluna, do pai e mãe
def invert_random_column(father, mother):
    random_item_chromosome = real_random(0, 19)

    for i in range(len(father)):
        father_value = father[i][random_item_chromosome]
        father[i][random_item_chromosome] = mother[i][random_item_chromosome]
        mother[i][random_item_chromosome] = father_value
        
        #Resolve os números repetidos após inversão da coluna
        _result_vanish_repeated = vanish_repeated_value(random_item_chromosome, i, mother, father)

        father = _result_vanish_repeated.mother
        mother = _result_vanish_repeated.father

    _resturn_mutation = _mutation(father, mother)

    _result_inverted = namedtuple('_result_inverted', 'father mother')
    _result_inverted.mother = _resturn_mutation.mother
    _result_inverted.father = _resturn_mutation.father

    return _result_inverted

#Inverte o número duplicado do pai com a mãe, até o individuo não possui mais números repetidos
def vanish_repeated_value(random_item_chromosome, i, mother, father):

    for j in range(len(father[i])):
        if j != random_item_chromosome and father[i][j] == father[i][random_item_chromosome]:
            father_value = father[i][j]
            father[i][j] = mother[i][j]
            mother[i][j] = father_value

            vanish_repeated_value(j, i, mother, father)

            break

    _result_vanish = namedtuple('_result_vanish', 'mother father')
    _result_vanish.father = father
    _result_vanish.mother = mother

    return _result_vanish

# Executa a mutação
def _mutation(father, mother):
    global RATE_MUTATION
    #Inverte um cromossomo aleatório do individuo
    for i in range(len(father)):
        RATE_MUTATION += 1
        _random_v1 = real_random(0, 19)
        _random_v2 = real_random(0, 19)

        _value_v1 = father[i][_random_v1]
        father[i][_random_v1] = father[i][_random_v2]
        father[i][_random_v2] = _value_v1

    #Inverte um cromossomo aleatório do individuo
    for i in range(len(mother)):
        _random_v1 = real_random(0, 19)
        _random_v2 = real_random(0, 19)

        _value_v1 = mother[i][_random_v1]
        mother[i][_random_v1] = mother[i][_random_v2]
        mother[i][_random_v2] = _value_v1

    _result_mutation = namedtuple('retorno', 'mutation mother father')
    _result_mutation.father = father
    _result_mutation.mother = mother

    return _result_mutation


#Inicia todos os processos, crossover (cycle) e mutação
def do_mutation_cycle(father, mother):
    
    _result_inverted_column = invert_random_column(father, mother)

    father = _result_inverted_column.father
    mother = _result_inverted_column.mother

    _result_mutation_cycle = namedtuple('retorno', 'son daughter')
    _result_mutation_cycle.son = father
    _result_mutation_cycle.daughter = mother

    return _result_mutation_cycle


#Limpa o console de saida
def _clear_console():
    if platform.system() == 'Windows':
        return lambda: os.system('cls')
    else:
        return lambda: os.system('clear')



#Adiciona a última coluna igual a primeira coluna
def _append_last_column(matrix):
    for line in matrix:
        if len(line) == 20:
            line.append(line[0])

    return matrix


def _calc_mutation():
    global RATE_MUTATION
    RATE_MUTATION /= (MAX_ITERATIONS * POPULATION)
    RATE_MUTATION *= 100

    return RATE_MUTATION

#Cria gráfico do melhor caminho
def _show_graph(cost, population):
    _x = []
    _y = []

    for i in population[0]:
        _x.append(cost[i] * 20)
        if i == 20:
            _y.append(cost[i] * 20)
        else:
            _y.append(cost[i + 1] * 20)

    pt = plt.subplot(111)
    pt.scatter(_x, _y, s = 30, color = 'green', marker = '.')

    _x.append(_x[0])
    _y.append(_y[0])

    plt.plot(_x, _y, color = 'purple', linestyle = 'solid', linewidth = 1)
    plt.show()

if __name__ == '__main__':

    matrix = create_random_matriz()
    _clear = _clear_console()

    for i in range(10000):
        _clear()
        matrix = _fitness(matrix)
        print(f'Interação de número: {i}')

    best_solution = matrix[0]
    _rate = _calc_mutation()

    # Resultado do algoritmo genetico
    print('Tamanho da população: 20')
    print(f'Taxa de mutação: {_rate}')
    print('Número de cidades: 20')
    print(f'Melhor custo: {BEST_COST}')
    print(f'Melhor solução: {best_solution}')

    matrix = _append_last_column(matrix)
    _show_graph(matrix[0], matrix)
