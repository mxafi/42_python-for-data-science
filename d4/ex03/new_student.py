import random
import string
from dataclasses import dataclass, field


def mute_trace(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
    return wrapper


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@mute_trace
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        assert isinstance(self.name, str), "Name must be a string"
        assert isinstance(self.surname, str), "Surname must be a string"
        assert isinstance(self.active, bool), "Active must be a boolean"
        assert self.name, "Name must not be empty"
        assert self.surname, "Surname must not be empty"
        self.login = self.name[0] + self.surname.lower()
