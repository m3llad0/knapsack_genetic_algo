import random
from typing import List, Tuple
from knapsack_instance import KnapsackInstance

class GeneticAlgorithm:
    """
    Implements a genetic algorithm for the 0-1 knapsack problem.

    Attributes:
        knapsack (KnapsackInstance): The knapsack problem instance.
        population_size (int): Number of individuals in the population.
        generations (int): Number of generations to run the algorithm.
        crossover_prob (float): Probability of crossover.
        mutation_prob (float): Probability of mutation for each gene.
    """
    def __init__(self, knapsack: KnapsackInstance, population_size=500, generations=500, 
                 crossover_prob=0.8, mutation_prob=None):
        self.knapsack = knapsack
        self.population_size = population_size
        self.generations = generations
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob if mutation_prob else 1 / len(knapsack.items)

    def fitness(self, solution: List[int]) -> float:
        """
        Computes the fitness of a solution.

        Args:
            solution (List[int]): Binary list representing the solution.
        
        Returns:
            float: Total profit of the solution, or 0 if the solution is invalid.
        """
        total_weight = 0
        total_profit = 0
        for i, bit in enumerate(solution):
            if bit == 1:
                weight, profit = self.knapsack.items[i]
                if total_weight + weight > self.knapsack.max_weight:
                    return 0  # Invalid solution
                total_weight += weight
                total_profit += profit
        return total_profit

    def generate_population(self) -> List[List[int]]:
        """
        Generates the initial population.
        
        Returns:
            List[List[int]]: Initial population of solutions.
        """
        return [[random.randint(0, 1) for _ in range(len(self.knapsack.items))] for _ in range(self.population_size)]

    def tournament_selection(self, population: List[List[int]], fitnesses: List[float], tournament_size=2) -> List[int]:
        """
        Performs tournament selection.

        Args:
            population (List[List[int]]): The population.
            fitnesses (List[float]): List of fitness values corresponding to the population.
            tournament_size (int): Number of individuals to compare in each tournament.
        
        Returns:
            List[int]: Selected individual from the population.
        """
        selected = random.sample(range(len(population)), tournament_size)
        best = max(selected, key=lambda x: fitnesses[x])
        return population[best]

    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        """
        Performs one-point crossover between two parents.

        Args:
            parent1 (List[int]): First parent.
            parent2 (List[int]): Second parent.
        
        Returns:
            Tuple[List[int], List[int]]: Two offspring.
        """
        if random.random() < self.crossover_prob:
            point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
            return child1, child2
        return parent1[:], parent2[:]

    def mutate(self, solution: List[int]) -> List[int]:
        """
        Mutates a solution using bit-flip mutation.

        Args:
            solution (List[int]): Binary list representing the solution.
        
        Returns:
            List[int]: Mutated solution.
        """
        for i in range(len(solution)):
            if random.random() < self.mutation_prob:
                solution[i] = 1 - solution[i]  # Flip bit
        return solution

    def run(self) -> Tuple[List[int], float]:
        """
        Runs the genetic algorithm.

        Returns:
            Tuple[List[int], float]: Best solution and its profit.
        """
        # Step 1: Initialize population
        population = self.generate_population()
        
        for generation in range(self.generations):
            # Step 2: Evaluate fitness
            fitnesses = [self.fitness(sol) for sol in population]
            
            # Step 3: Create new population
            new_population = []
            while len(new_population) < self.population_size:
                # Selection
                parent1 = self.tournament_selection(population, fitnesses)
                parent2 = self.tournament_selection(population, fitnesses)
                
                # Crossover
                child1, child2 = self.crossover(parent1, parent2)
                
                # Mutation
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                
                new_population.extend([child1, child2])
            
            population = new_population[:self.population_size]

        # Step 4: Return best solution
        fitnesses = [self.fitness(sol) for sol in population]
        best_idx = max(range(len(population)), key=lambda i: fitnesses[i])
        return population[best_idx], fitnesses[best_idx]
