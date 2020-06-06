import random
from deap import creator, base, tools, algorithms


class Distribuction:
    def __init__(self, products, limit):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self.products = products
        self.limit = limit

        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_bool",
                              random.randint, 0, 1)
        self.toolbox.register("individual",
                              tools.initRepeat, creator.Individual, self.toolbox.attr_bool, n=len(self.products))
        self.toolbox.register("population",
                              tools.initRepeat, list, self.toolbox.individual)

    def EvalOneMax(self, individual):
        value = 0
        weight = 0

        for i in range(len(individual)):
            if individual[i] == 1:
                value += self.products[i].value
                weight += self.products[i].weight

        return {'value': [value], 'weight': weight}

    def GetBetters(self):
        self.toolbox.register("evaluate", self.EvalOneMax)
        self.toolbox.register("mate", tools.cxTwoPoint)  # crossover
        self.toolbox.register("mutate", tools.mutFlipBit,
                              indpb=0.05)  # mutação

        self.toolbox.register("select", tools.selTournament, tournsize=3)

        population = self.toolbox.population(n=300)

        NGEN = 40
        for gen in range(NGEN):
            offspring = algorithms.varAnd(
                population, self.toolbox, cxpb=0.5, mutpb=0.1)
            fits = self.toolbox.map(self.toolbox.evaluate, offspring)
            for fit, ind in zip(fits, offspring):
                if fit['weight'] > self.limit:
                    ind.fitness.values = [0]
                else:
                    ind.fitness.values = fit['value']

            population = self.toolbox.select(offspring, k=len(population))

        betters = tools.selBest(population, k=10)[0]
        result = []
        for key, value in enumerate(betters):
            if value == 1:
                result.append(self.products[key])

        return {"products": result, "state": self.EvalOneMax(betters)}


# products = [{'value': 6, 'weight': 2},
#             {'value': 5, 'weight': 3},
#             {'value': 8, 'weight': 6},
#             {'value': 9, 'weight': 7},
#             {'value': 6, 'weight': 5},
#             {'value': 7, 'weight': 9},
#             {'value': 3, 'weight': 4},
#             ]

# dist = Distribuction(products)
# best = dist.GetBetters()

# print(best["products"])
# print(best["state"])
