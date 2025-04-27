### 1. **Introduction:**
   - **Briefly introduce the concept of Evolutionary Algorithms (EAs):**
     "Evolutionary algorithms are a class of optimization algorithms inspired by the process of natural evolution. They are used to find optimal or near-optimal solutions to complex problems by simulating processes like selection, crossover (recombination), and mutation. The DEAP (Distributed Evolutionary Algorithms) framework helps us implement these algorithms efficiently."
   
   - **State the problem being solved:**
     "In this practical, we are solving an optimization problem where the objective is to maximize the function \( f(x) = x \sin(10\pi x) + 1 \) within the interval [0, 1]. This problem is an example of a real-valued function optimization, which we aim to solve using a genetic algorithm."

### 2. **Explain the DEAP Framework:**
   - **DEAP Overview:**
     "DEAP is a flexible framework for implementing evolutionary algorithms. It provides the necessary tools for defining individuals, populations, genetic operators like crossover and mutation, and selection mechanisms. We use DEAP to implement a basic genetic algorithm in this practical."

   - **Core Components:**
     - **Population**: The collection of candidate solutions (individuals) for the optimization problem.
     - **Selection**: The process of selecting individuals based on their fitness.
     - **Crossover**: Combining genetic material of selected individuals to create new offspring.
     - **Mutation**: Randomly altering the genetic material of individuals to introduce diversity.
     - **Evaluation**: Assessing the fitness of individuals.
     - **Termination**: Stopping the algorithm after a set number of generations or when convergence is achieved.

### 3. **Walk Through the Code (Line by Line):**

#### Import Libraries:
```python
import random
from deap import base, creator, tools, algorithms # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
```
- **random**: For generating random numbers, which is essential for initializing individuals and for mutation.
- **deap**: The core library for evolutionary algorithms, where we import tools for creating the population and applying genetic operations like crossover and mutation.
- **numpy**: To handle numerical operations, particularly for the fitness function calculations.
- **matplotlib**: For plotting the fitness progression over generations.

#### Define the Fitness Function:
```python
def fitness_func(individual):
    x = individual[0]
    return x * np.sin(10 * np.pi * x) + 1,  # comma makes it a tuple
```
- **Explanation**: This is the fitness function we aim to optimize. The goal is to maximize \( f(x) = x \sin(10\pi x) + 1 \), which has a periodic nature. The fitness of an individual is computed using this function.

#### Define the Custom Fitness and Individual Types:
```python
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
```
- **Explanation**: DEAP uses Python's `creator` to define custom types.
  - `FitnessMax`: Specifies that we are maximizing the fitness function.
  - `Individual`: Defines the type for an individual, which is a list of genes (in this case, just one gene `x`).

#### Define the Toolbox (Genetic Algorithm Setup):
```python
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
```
- **Explanation**: The toolbox is used to register functions for creating individuals and populations.
  - `attr_float`: Generates a random float between 0 and 1, representing the gene of an individual.
  - `individual`: Creates a single individual using `attr_float`.
  - `population`: Creates a population by repeating the individual creation function.

#### Register Genetic Operators:
```python
toolbox.register("evaluate", fitness_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
```
- **Explanation**:
  - `evaluate`: Uses the `fitness_func` to evaluate the fitness of individuals.
  - `mate`: Defines the crossover operator (`cxBlend`), which blends two parents' genes to create offspring. `alpha=0.5` controls the blending.
  - `mutate`: Defines the mutation operator (`mutGaussian`), which introduces random changes to individuals' genes using Gaussian distribution.
  - `select`: Specifies the selection method (`selTournament`), where individuals are chosen based on a tournament with size 3.

#### Define the Evolutionary Algorithm:
```python
def run_deap():
    pop = toolbox.population(n=20)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)
```
- **Explanation**: Initializes the population and sets up a Hall of Fame (`hof`) to store the best individual and statistics to track the progress.
  - `pop`: The population consists of 20 individuals.
  - `hof`: Keeps track of the best individual across generations.
  - `stats`: Stores and tracks average and maximum fitness values for each generation.

#### Run the Evolutionary Algorithm:
```python
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=20, 
                                    stats=stats, halloffame=hof, verbose=True)
```
- **Explanation**: This is where the evolutionary algorithm is executed using the `eaSimple` function from DEAP.
  - **Parameters**:
    - `cxpb=0.7`: Crossover probability of 70%.
    - `mutpb=0.2`: Mutation probability of 20%.
    - `ngen=20`: The algorithm runs for 20 generations.
    - `stats`: Tracks the statistics (average and maximum fitness).
    - `hof`: Keeps track of the best individual.
    - `verbose=True`: Outputs progress information.

#### Print the Best Solution:
```python
    print(f"\n🏆 Best solution: x = {hof[0][0]:.4f}, fitness = {hof[0].fitness.values[0]:.4f}")
```
- **Explanation**: After the algorithm finishes, this line prints the best solution found by the algorithm, showing the value of `x` and its corresponding fitness.

#### Plot the Fitness Progress:
```python
    gen = log.select("gen")
    fit_max = log.select("max")
    plt.plot(gen, fit_max, label="Max Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Evolution of Fitness using DEAP")
    plt.legend()
    plt.grid()
    plt.show()
```
- **Explanation**: This block plots how the maximum fitness evolves over the generations. It helps to visualize the algorithm's convergence toward the optimal solution.

#### Run the Algorithm:
```python
run_deap()
```
- **Explanation**: This simply runs the algorithm.

### 4. **Results and Explanation:**
   - **Output Summary**: The algorithm found the optimal value of \( x \) to be **0.6516**, with a corresponding fitness of **1.6508**, which is very close to the maximum value of the function.
   - **Convergence**: Over the 20 generations, the algorithm progressively improved the fitness of the population, stabilizing at the optimal solution.
   - **Plot**: Show the plot of maximum fitness vs. generations to demonstrate the algorithm's progress.

### 5. **Conclusion:**
   - **Final Remarks**: "This practical demonstrates the application of a genetic algorithm to solve an optimization problem using DEAP. The algorithm successfully converged to the optimal solution in 20 generations. DEAP allows us to implement and customize evolutionary algorithms efficiently, providing a flexible framework for solving real-world optimization problems."
