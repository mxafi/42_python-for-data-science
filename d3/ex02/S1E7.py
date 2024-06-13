from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

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
    def __init__(self, first_name, is_alive=True,
                 family_name="Lannister", eyes="blue", hairs="light"):
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

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
