import random
from deap import creator, base, tools

random.seed(69)

sequence_length = 8


creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()





# Individuals
def generate_individual():
    return [random.randint(0,1) for _ in range(sequence_length)]

# ind = generate_individual()
# print("Ex individual (coefficients):", ind)




# Toolbox
toolbox.register('individual', generate_individual)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)




# Generate initial population
pop = toolbox.population(n=10)
print('Example pop:')
for ind in pop:
    print(ind)





# Evolution loop


# Analysis and visualization
