from typing import List, Dict


class Node:
    def __init__(self, color: str, coordinates: List[int]):
        self.color = color
        self.coordinates = coordinates


class Rubik:
    def __init__(self, surfaces: Dict[str, List]):
        self.surfaces = surfaces
