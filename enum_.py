from enum import Enum

class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

for i in range(len(Colors)):
    print(f"Enum Name: {Colors(i + 1).name}, Enum Value: {Colors(i + 1).value}")