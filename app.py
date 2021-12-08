from abc import ABC, abstractmethod
from typing import *


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


