import random
import math

#Function to calculate the number of conflicts (heuristic)
def calculate_conflicts(queens):
    conflicts = 0
    n = len(queens)
    
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j]:  # same row
                conflicts += 1
            if abs(queens[i] - queens[j]) == j - i:  # same diagonal
                conflicts += 1
    
    return conflicts


# Simulated Annealing algorithm
def simulated_annealing(n=8):
    # Initial random state
    current = [random.randint(0, n - 1) for _ in range(n)]
    temperature = 100
    cooling_rate = 0.99
    min_temperature = 0.001
    
    while temperature > min_temperature:
        conflicts = calculate_conflicts(current)
        if conflicts == 0:
            return current
        
        next_state = current[:]
        col = random.randint(0, n - 1)
        next_state[col] = random.randint(0, n - 1)
        
        next_conflicts = calculate_conflicts(next_state)
        
        # Acceptance probability
        delta = next_conflicts - conflicts
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature):
            current = next_state
        
        temperature *= cooling_rate
    
    return None  # No solution found



# Running Simulated Annealing
solution = simulated_annealing()
if solution:
    print(f"Solution found: {solution}")
else:
    print("No solution found")




