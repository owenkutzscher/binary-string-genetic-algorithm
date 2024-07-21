import random
import numpy as np
from deap import creator, base, tools

# random.seed(69)

target = [1,1,1,1,1,1,1,1] # [1,1,1,1,0,0,0,0]
print(f'\ntarget:{target}\n')


def evaluate_sequence(individual):
    error = 0.0
    error = np.sum((np.array(target) - np.array(individual))**2)
    return (error,)




# Setup DEAP framework
creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()


# Reister individuals and population
IND_SIZE = 8
def pick_rand():
    return random.randint(0,1)

toolbox.register("individual", tools.initRepeat, creator.Individual,
                 lambda: random.randint(0,1), n=IND_SIZE)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)


# Register genetic operators
toolbox.register('test_fitness', evaluate_sequence)
toolbox.register('select', tools.selTournament)
toolbox.register('rand_select', tools.selRoulette)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutFlipBit, indpb=0.25)








pop = toolbox.population(n=20)
fitnesses = map(toolbox.test_fitness, pop)

# avg_fitness = 
# best_ind = 
print('Initial populaiton avg fitness:{}')

    

NGEN=100
for gen in range(NGEN):
    
    fitnesses = map(toolbox.test_fitness, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    selected = toolbox.select(pop, 5, len(pop))
    
    # Fill up the rest of the pop
    while len(selected) < len(pop):
        if random.random() < 0.5:
            selected.append(toolbox.individual())
        else:
            selected.append(random.choice(pop))


#     additional_ind = toolbox.rand_select(pop, 1)
#     selected.append(additional_ind[0])

    offspring = [toolbox.clone(ind) for ind in selected]
    
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < 0.5:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values
            
        
    for mutant in offspring:
        if random.random() < 0.1:
            toolbox.mutate(mutant)
            del mutant.fitness.values
            
            
    pop[:] = offspring

    

    

# print(f'\nFinal individuals:')
# for ind in pop:
#     print(ind)
