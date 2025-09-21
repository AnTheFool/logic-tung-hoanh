import random
from .base_rule import BaseRule

class AdditionRule(BaseRule):
    def __init__(self):
        pass

    def generate(self, length = 6, is_horizontal = True):
        d = random.randint(5, 20)
        start = random.randint(1, 10)
        sequence = [start + i * d for i in range(length)]
        idx = random.randint(1, length - 2)
        missing = sequence[idx]
        sequence[idx] = '?'
        return {
            'sequence': sequence,
            'missing_value': missing,
            'missing_index': idx,
            'd': d
        }
    
    def get_name(self):
        return "Addition Rule"