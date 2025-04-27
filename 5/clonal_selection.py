import random
import numpy as np

# Problem: maximize f(x) = 1 / (1 + x^2)  → highest at x = 0

POP_SIZE = 10          # Population size
CLONE_FACTOR = 3       # Number of clones per selected antibody
MUTATION_RATE = 0.2    # Probability of mutation
GENERATIONS = 10       # Number of generations

# Generate random antibody
def random_antibody():
    # Randomly generate an antibody in the range [-10, 10]
    return random.uniform(-10, 10)

# Affinity function (higher is better)
def affinity(x):
    # Affinity function is f(x) = 1 / (1 + x^2), the function is maximized when x = 0
    return 1 / (1 + x ** 2)

# Mutate with small random noise
def mutate(x):
    # If a random number is less than the mutation rate, mutate the solution
    if random.random() < MUTATION_RATE:
        x += random.uniform(-1, 1)  # Add small random value to x
    return x

def clonal_selection():
    # Initialize population with random antibodies
    population = [random_antibody() for _ in range(POP_SIZE)]
    best = None
    best_aff = 0

    for gen in range(GENERATIONS):
        # Evaluate affinity of each antibody in the population
        affinities = [affinity(x) for x in population]
        
        # Sort population by their affinity values in descending order
        sorted_pop = [x for _, x in sorted(zip(affinities, population), reverse=True)]
        
        # Print the best antibody and its affinity in the current generation
        print(f"Gen {gen+1}: Best Antibody = {round(sorted_pop[0], 4)} | Affinity = {round(affinity(sorted_pop[0]), 4)}", '\n')

        # Keep track of the best solution found so far
        if affinity(sorted_pop[0]) > best_aff:
            best_aff = affinity(sorted_pop[0])
            best = sorted_pop[0]

        # Select the top 3 antibodies for cloning based on highest affinity
        selected = sorted_pop[:3]
        clones = []
        
        # Create clones of the selected antibodies, applying mutations
        for antibody in selected:
            for _ in range(CLONE_FACTOR):
                clone = mutate(antibody)  # Mutate the antibody to create a clone
                clones.append(clone)

        # Combine the selected antibodies and their clones into a new population
        combined = selected + clones
        
        # Sort the combined population by affinity again, in descending order
        combined.sort(key=affinity, reverse=True)
        
        # Keep the top POP_SIZE individuals (including original and clones) for the next generation
        population = combined[:POP_SIZE]

    # After all generations, print the final best antibody and its affinity
    print(f"\n🧬 Final Best Antibody: {round(best, 4)} | Affinity: {round(best_aff, 4)}")

# Run the clonal selection algorithm
clonal_selection()
