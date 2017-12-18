from enum import Enum


class LogLevel(Enum):
    CRITICAL = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4

    def __ge__(self, level):
        return self.value >= level.value
