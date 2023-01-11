
from src.map import Map

class QLearningAgent:
    def __init__(self, map: Map) -> None:
        self.map= map
        self.alpha = 0.2
        self.discount = 0.9
        self.q_values = []
        