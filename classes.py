from random import randint
import pandas as pd


class Player:

    def __init__(self: object, name: str, score: int = 0) -> None:
        self.name: str = name
        self.score: int = score

    @property
    def return_names(self):
        return self.name
