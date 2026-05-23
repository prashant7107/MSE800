from abc import ABC, abstractmethod
# FISH CLASSES
class Fish(ABC):
    def __init__(self, category: str):
        self.category = category

class Goldfish(Fish):
    def __init__(self):
        super().__init__("Goldfish")

class Shark(Fish):
    def __init__(self):
        super().__init__("Shark")

class Angelfish(Fish):
    def __init__(self):
        super().__init__("Angelfish")

class Tuna(Fish):
    def __init__(self):
        super().__init__("Tuna")

class Salmon(Fish):
    def __init__(self):
        super().__init__("Salmon")
