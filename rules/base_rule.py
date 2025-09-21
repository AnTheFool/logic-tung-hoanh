from abc import ABC, abstractmethod

class BaseRule(ABC):
    @abstractmethod
    def generate(self, length: int, is_horizontal: bool):
        """Generate sequence with missing value"""
        pass

    @abstractmethod
    def get_name(self):
        pass