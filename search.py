from abc import ABC, abstractmethod

# abstract class for all diffrent search alorithms
class Search(ABC):
    def __init__(self, intial_state) -> None:
        self.__intial_state = intial_state
    
    @abstractmethod
    def solve() -> dict:
        pass