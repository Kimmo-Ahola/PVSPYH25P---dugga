# empty for now
from faker import Faker

fake = Faker()


class User:
    """
    Use standard Python class or a dataclass. Whichever you prefer.
    DO NOT create a database class.
    """
    def get_random_users() -> list["User"]:
        """
        This method should return a list of users.
        The amount should be random between 1-30 (inclusive)
        """
        pass

# this is my first fix