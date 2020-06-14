import random

GENES = '''abcdefghijklmnopqrstuvwxyz 1234567890:()°-.'''


class HangmanGame(object):
    def __init__(self, chromosome, target):
        self.target = target
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    def mutated_genes(self):
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self, target):
        gnome_len = len(target)
        return [self.mutated_genes(self) for _ in range(gnome_len)]

    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return HangmanGame(child_chromosome, self.target)

    def cal_fitness(self):
        fitness = 0
        for gs, gt in zip(self.chromosome, self.target):
            if gs != gt:
                fitness += 1
        return fitness

    @classmethod
    def Start(self, target, population_size=100):
        generation = 1
        generations = []

        found = False
        population = []

        target = target.lower()

        for _ in range(population_size):
            gnome = HangmanGame.create_gnome(target)
            population.append(HangmanGame(gnome, target))

        while not found:
            population = sorted(population, key=lambda x: x.fitness)
            if population[0].fitness <= 0:
                found = True
                break

            new_generation = []
            s = int((10 * population_size)/100)
            new_generation.extend(population[:s])
            s = int((90 * population_size)/100)

            for _ in range(s):
                parent1 = random.choice(population[:50])
                parent2 = random.choice(population[:50])
                child = parent1.mate(parent2)
                new_generation.append(child)

            population = new_generation
            generation += 1
            string = "".join(population[0].chromosome)
            fitness = population[0].fitness

            generations.append(
                {"generation": generation, "string": string, "fitness": fitness})

            if (generation > 500):
                break

        string = "".join(population[0].chromosome)
        fitness = population[0].fitness

        generations.append(
            {"generation": generation, "string": string, "fitness": fitness})

        return {"generation": generation, "string": string, "fitness": fitness, "generations": generations}


# game = HangmanGame.Start("Tengen Toppa Gurren Langan")
# print(
#     f"Generation: {game['generation']}\tString: {game['string']}\tFitness: {game['fitness']}")
