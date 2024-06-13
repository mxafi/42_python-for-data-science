from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the (false) King character."""
    def __init__(self, first_name):
        """Initialize the King character."""
        super().__init__(first_name)

    def set_eyes(self, color):
        """Set the eyes color."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hairs color."""
        self.hairs = color

    def get_eyes(self):
        """Return the eyes color."""
        return self.eyes

    def get_hairs(self):
        """Return the hairs color."""
        return self.hairs
