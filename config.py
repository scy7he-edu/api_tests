from dataclasses import dataclass, field

from src.utils.data_generator import fake


@dataclass
class Credentials:
    URL: str = "https://dummyjson.com"
    firstName: str = field(default_factory=fake.first_name)
    lastName: str = field(default_factory=fake.last_name)
    age: int = field(default_factory=lambda: fake.pyint(18, 90))
    username: str = "emilys"
    password: str = "emilyspass"

    @property
    def user_data(self) -> dict:
        return {"firstName": self.firstName, "lastName": self.lastName, "age": self.age}
