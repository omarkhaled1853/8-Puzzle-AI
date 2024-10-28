from abc import ABC, abstractmethod

# abstract class for all diffrent search alorithms
class Search(ABC):
    def __init__(self, intial_state) -> None:
        self._intial_state = intial_state
    
    @abstractmethod
    def solve(self) -> dict:
        """Abstract method to be implemented by subclasses"""
        pass