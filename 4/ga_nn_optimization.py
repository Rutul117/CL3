import random
import numpy as np # type: ignore

# Simulated neural network accuracy based on weights
# The fitness function returns a measure of how close the weights are to the ideal value of 0.5.
# The closer the weights are to 0.5, the better the fitness.
def evaluate_fitness(weights):
    return 1 / (1 + np.sum(np.square(weights - 0.5)))  # Best fitness when weights ~0.5

# GA parameters
POP_SIZE = 10  # Population size: how many individuals (chromosomes) in each generation
CHROMO_LENGTH = 5  # Length of each individual (chromosome), i.e., number of weights in the neural network
MUTATION_RATE = 0.1  # Probability of a mutation occurring on a given gene
CROSSOVER_RATE = 0.8  # Probability of crossover between two parents
GENERATIONS = 20  # Total number of generations the algorithm will run

# Generate initial population
# Initializes a population with random weights for each individual (chromosome)
def init_population():
    return [np.random.rand(CHROMO_LENGTH) for _ in range(POP_SIZE)]  # Random weights between 0 and 1

# Crossover two parents to produce two children
# Crossover mixes the genetic material of two parents to create offspring
def crossover(p1, p2):
    # If a random number is less than the crossover rate, perform crossover
    if random.random() < CROSSOVER_RATE:
        # Pick a random crossover point between 1 and CHROMO_LENGTH-1
        point = random.randint(1, CHROMO_LENGTH - 1)
        # Create two children by swapping the genetic material after the crossover point
        child1 = np.concatenate((p1[:point], p2[point:]))
        child2 = np.concatenate((p2[:point], p1[point:]))
        return child1, child2
    return p1, p2  # If no crossover, return parents as children

# Mutate a chromosome (individual solution)
# Mutate randomly by changing genes with a given mutation rate
def mutate(chromo):
    for i in range(CHROMO_LENGTH):
        # If a random number is less than the mutation rate, mutate the gene at position i
        if random.random() < MUTATION_RATE:
            chromo[i] = random.random()  # Replace gene with a random value between 0 and 1
    return chromo

# GA loop (genetic algorithm main loop)
def genetic_algorithm():
    # Step 1: Initialize the population with random chromosomes
    population = init_population()
    best_fitness = 0
    best_solution = None

    # Step 2: Iterate through generations to evolve the population
    for gen in range(GENERATIONS):
        # Step 3: Evaluate fitness of each individual (chromosome)
        fitness_scores = [evaluate_fitness(ind) for ind in population]
        
        # Step 4: Sort population based on fitness scores (highest fitness first)
        sorted_indices = np.argsort(fitness_scores)[::-1]  # Sort indices in descending order of fitness
        population = [population[i] for i in sorted_indices]  # Reorder population based on fitness scores

        # Step 5: Track best solution so far
        if fitness_scores[sorted_indices[0]] > best_fitness:
            best_fitness = fitness_scores[sorted_indices[0]]  # Update best fitness
            best_solution = population[0]  # Update best solution (individual)

        # Print the best fitness value of the current generation
        print(f"Generation { gen+1} | Best Fitness: {best_fitness:.4f}")

        # Step 6: Apply elitism - keep the top 2 individuals without changes
        new_population = population[:2]  # Elitism: Keep top 2 individuals

        # Step 7: Select parents from the top 5 individuals and perform crossover and mutation
        while len(new_population) < POP_SIZE:
            p1, p2 = random.sample(population[:5], 2)  # Randomly select 2 parents from the top 5
            c1, c2 = crossover(p1, p2)  # Perform crossover to generate two children
            new_population.append(mutate(c1))  # Mutate and add child 1 to new population
            if len(new_population) < POP_SIZE:
                new_population.append(mutate(c2))  # Mutate and add child 2 to new population if needed

        # Step 8: Replace old population with new population for the next generation
        population = new_population

    # Final output: Display the best solution and fitness after all generations
    print("\n✅ Optimized Weights:", np.round(best_solution, 3))  # Display the optimized weights
    print("🥥 Simulated Coconut Milk Spray Drying Accuracy:", round(best_fitness * 100, 2), "%")  # Display accuracy

# Run the genetic algorithm
genetic_algorithm()
