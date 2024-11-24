# Genetic Algorithm for the 0-1 Knapsack Problem

## Overview
This project implements a **Genetic Algorithm (GA)** to solve the knapsack problem. The GA uses heuristic techniques such as selection, crossover, and mutation to find near-optimal solutions within a vast search space. The goal is to maximize the profit of selected items without exceeding the weight constraint.

## Problem Description
The knapsack problem can be described mathematically as follows:

### Problem Formulation
Given:
- $ (n) $: Number of items.
- $ (w_i) $: Weight of item ($ i = 1, 2, \dots, n $).
- $ (p_i) $: Profit of item ($ i = 1, 2, \dots, n $).
- $ (W) $: Maximum weight capacity of the knapsack.

Define:
- $( x_i )$: Decision variable, where $( x_i = 1 )$ if item $( i )$ is included, and $( x_i = 0 )$ otherwise.

Objective:
Maximize the total profit:  $\text{Maximize } Z = \sum_{i=1}^n p_i \cdot x_i$

Subject to:
$
 \sum_{i=1}^n w_i \cdot x_i \leq W, \quad x_i \in \{0, 1\}.
$

This is a combinatorial optimization problem where the aim is to find the binary vector \( \mathbf{x} = [x_1, x_2, \dots, x_n] \) that maximizes \( Z \) while satisfying the weight constraint.


## Genetic Algorithm Approach
### Representation
- Solutions are represented as binary strings \( \mathbf{x} = [x_1, x_2, \dots, x_n] \), where \( x_i = 1 \) indicates that item \( i \) is included in the knapsack.

### Genetic Operators
1. **Fitness Function**:
   - The fitness of a solution \( \mathbf{x} \) is computed as:
     \[
     \text{Fitness}(\mathbf{x}) = \sum_{i=1}^n p_i \cdot x_i,
     \]
     if the solution satisfies the weight constraint:
     \[
     \sum_{i=1}^n w_i \cdot x_i \leq W.
     \]
     Otherwise, the fitness is penalized or set to zero.

2. **Selection**:
   - Tournament selection is used, where two or three individuals compete, and the best one is selected based on fitness.

3. **Crossover**:
   - One-point crossover is applied with a probability \( p_c \) (typically 0.7–0.9), creating offspring by exchanging genetic material between two parents.

4. **Mutation**:
   - Flip mutation is applied with a probability \( p_m = \frac{1}{n} \), flipping a random bit in the solution to maintain diversity.

5. **Elitism**:
   - The best solution from the current generation is carried over to the next generation to preserve high-quality solutions.

### Algorithm Steps
1. Initialize a random population of binary strings of size \( \text{Population Size} \).
2. Evaluate the fitness of each individual in the population.
3. Repeat for a fixed number of generations:
   1. Select parents using tournament selection.
   2. Perform crossover to generate offspring.
   3. Apply mutation to introduce diversity.
   4. Evaluate the fitness of the new population.
   5. Apply elitism to retain the best solution.
4. Return the best solution found.


## Features
- **Representation**: Binary strings where each bit indicates whether an item is included (1) or excluded (0).
- **Genetic Operators**: Selection, crossover, and mutation to evolve the population.
- **Configurable Parameters**: Population size, generations, and probabilities for mutation and crossover.


## Authors

* Diego Mellado Oliveros
* Gerardo Damián García Rubio
* Alejandro Gutiérrez Saldaña
* Samuel José Ramírez Doñe

