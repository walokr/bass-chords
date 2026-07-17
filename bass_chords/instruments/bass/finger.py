from enum import Enum


class Finger(Enum):
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4

    def __str__(self):
        return str(self.value)
