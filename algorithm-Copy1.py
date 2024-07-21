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
toolbox.register('evaluate', evaluate_sequence)
toolbox.register('select', tools.selTournament)
toolbox.register('rand_select', tools.selRoulette)
toolbox.register('sex', tools.cxOnePoint)
toolbox.register('mutate', tools.mutFlipBit)








pop = toolbox.population(n=8)

NGEN=100
for gen in range(NGEN):
    
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    selected = toolbox.select(pop, 2, len(pop))
    
    

    additional_ind = toolbox.rand_select(pop, 1)
    selected.append(additional_ind[0])
    
    
    
    offspring = []
    for _ in range(len(pop)):
        two_inds = toolbox.rand_select(mutated, 2)
        offspring.append(toolbox.sex(two_inds[0],two_inds[1])[0])
        
    mutated = []
    for ind in selected:
        mutated_ind = (toolbox.mutate(ind, 0.1))
        mutated.append(mutated_ind[0])

    pop[:] = offspring

    

    

print(f'\nFinal individuals:')
for ind in selected:
    print(ind)
