from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, points, name = "Figure"):
        self.points = points
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @abstractmethod
    def area(self):
        return NotImplementedError("Método abstracto")