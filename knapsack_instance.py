from typing import List, Tuple
import os

class KnapsackInstance:
    """
    Represents a knapsack problem instance.
    
    Attributes:
        max_weight (int): Maximum weight capacity of the knapsack.
        items (List[Tuple[int, float]]): List of items where each item is a tuple (weight, profit).
    """
    def __init__(self, max_weight: int, items: List[Tuple[int, float]]):
        self.max_weight = max_weight
        self.items = items

    @staticmethod
    def load(file_name: str) -> 'KnapsackInstance':
        """
        Loads a knapsack problem instance from a file.
        
        Args:
            file_name (str): Path to the file containing the problem instance.
        
        Returns:
            KnapsackInstance: A knapsack problem instance.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
        with open(os.path.join(base_dir, "KPInstances", file_name), "r") as f:
            lines = f.readlines()
        line = lines[0].split(",")
        nb_items = int(line[0].strip())
        max_weight = int(line[1].strip())
        items = []
        for i in range(nb_items):
            line = lines[i + 1].split(",")
            weight = int(line[0].strip())
            profit = float(line[1].strip())
            items.append((weight, profit))
        return KnapsackInstance(max_weight, items)