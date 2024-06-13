from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive, "brown", "dark")

    def die(self):
        """Kill the character."""
        return super().die()

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """Create a Baratheon character."""
        return cls(first_name, is_alive)

    def __str__(self):
        """Return a string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the character."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive, "blue", "light")

    def die(self):
        """Kill the character."""
        return super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister character."""
        return cls(first_name, is_alive)

    def __str__(self):
        """Return a string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the character."""
        return self.__str__()
