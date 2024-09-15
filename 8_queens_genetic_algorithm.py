import random

#Function to calculate the fitness (number of non-attacking pairs)
def fitness(queens):
    non_attacking_pairs = 0
    n = len(queens)
    
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] != queens[j] and abs(queens[i] - queens[j]) != abs(i - j):
                non_attacking_pairs += 1
    
    return non_attacking_pairs



#Genetic algorithm functions
def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(queens, mutation_rate=0.1):
    n = len(queens)
    if random.uniform(0, 1) < mutation_rate:
        col = random.randint(0, n - 1)
        queens[col] = random.randint(0, n - 1)
    return queens




#Genetic Algorithm
def genetic_algorithm(n=8, population_size=100, generations=1000):
    # Initial population
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(population_size)]
    
    for generation in range(generations):
        # Sort population by fitness
        population = sorted(population, key=fitness, reverse=True)
        
        if fitness(population[0]) == (n * (n - 1)) // 2:  # Maximum possible fitness
            return population[0]
        
        new_population = population[:population_size // 2]
        
        # Crossover and mutation
        while len(new_population) < population_size:
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            child = crossover(parent1, parent2)
            new_population.append(mutate(child))
        
        population = new_population
    
    return None  # No solution found



# Running Genetic Algorithm
solution = genetic_algorithm()
if solution:
    print(f"Solution found: {solution}")
else:
    print("No solution found")
