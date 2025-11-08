from typing import Protocol

class Packaging(Protocol):
    def __init__(self, packaging:str = None):
        self.packaging = packaging