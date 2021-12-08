from abc import ABC, abstractmethod
from typing import *
from views import *


class Builder(ABC):

    @abstractmethod
    def creator(self):
        pass


class NodeCreator(Builder):

    def creator(self):
        pass


class RubikCreator(Builder):

    def creator(self):
        pass


class Logger(Solver):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)