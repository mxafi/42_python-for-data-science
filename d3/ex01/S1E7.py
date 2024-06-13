from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive, "brown", "dark")

    def die(self):
        return super().die()

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive, "blue", "light")

    def die(self):
        return super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
