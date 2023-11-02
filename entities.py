from typing import *

class Layer:

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

class Design:

    def __init__(self, precision: float=0.0, name:str="", layers: List[Layer]=[]):
        self.precision = precision
        self.name = name
        self.layers = layers