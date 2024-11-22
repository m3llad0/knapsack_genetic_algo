from genetic_algorithm import GeneticAlgorithm
from knapsack_instance import KnapsackInstance

if __name__ == "__main__":
    # Load a problem instance
    knapsack = KnapsackInstance.load("ks_4_0")
    
    print("Problem instance: ", knapsack.max_weight, knapsack.items )
    # Create and run the genetic algorithm
    ga = GeneticAlgorithm(knapsack)
    best_solution, best_profit = ga.run()
    
    # Print results
    print("Best Solution (Binary):", best_solution)
    print("Best Profit:", best_profit)
    selected_items = [knapsack.items[i] for i in range(len(knapsack.items)) if best_solution[i] == 1]
    print("Selected Items (Weight, Profit):", selected_items)