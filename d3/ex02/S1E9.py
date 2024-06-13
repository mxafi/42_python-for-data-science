from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract base class representing a character."""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True,
                 family_name: str = "", eyes: str = "", hairs: str = ""):
        """Constructor for Character class."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @abstractmethod
    def die(self):
        """Kill the character from the Character class."""
        self.is_alive = False


class Stark(Character):
    """A derived class Stark inheriting from abstract Character."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark class."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character from the Stark class."""
        super().die()
