import random
import numpy as np # type: ignore

# Simulated neural network accuracy based on weights
def evaluate_fitness(weights):
    return 1 / (1 + np.sum(np.square(weights - 0.5)))  # Best fitness when weights ~0.5

# GA parameters
POP_SIZE = 10
CHROMO_LENGTH = 5
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
GENERATIONS = 20

# Generate initial population
def init_population():
    return [np.random.rand(CHROMO_LENGTH) for _ in range(POP_SIZE)]

# Crossover two parents
def crossover(p1, p2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMO_LENGTH - 1)
        child1 = np.concatenate((p1[:point], p2[point:]))
        child2 = np.concatenate((p2[:point], p1[point:]))
        return child1, child2
    return p1, p2

# Mutate a chromosome
def mutate(chromo):
    for i in range(CHROMO_LENGTH):
        if random.random() < MUTATION_RATE:
            chromo[i] = random.random()
    return chromo

# GA loop
def genetic_algorithm():
    population = init_population()
    best_fitness = 0
    best_solution = None

    for gen in range(GENERATIONS):
        fitness_scores = [evaluate_fitness(ind) for ind in population]
        sorted_indices = np.argsort(fitness_scores)[::-1]
        population = [population[i] for i in sorted_indices]

        if fitness_scores[sorted_indices[0]] > best_fitness:
            best_fitness = fitness_scores[sorted_indices[0]]
            best_solution = population[0]

        print(f"Generation { gen+1} | Best Fitness: {best_fitness:.4f}")

        new_population = population[:2]  # Elitism

        while len(new_population) < POP_SIZE:
            p1, p2 = random.sample(population[:5], 2)  # Top 5 selection
            c1, c2 = crossover(p1, p2)
            new_population.append(mutate(c1))
            if len(new_population) < POP_SIZE:
                new_population.append(mutate(c2))

        population = new_population

    print("\n✅ Optimized Weights:", np.round(best_solution, 3))
    print("🥥 Simulated Coconut Milk Spray Drying Accuracy:", round(best_fitness * 100, 2), "%")

genetic_algorithm()
