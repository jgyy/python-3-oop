from abc import ABC, abstractmethod

class Character(ABC):
    """
    An abstract base class representing a character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character with a name and living status.

        :param first_name: The character's first name
        :param is_alive: Whether the character is alive (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Change the character's living status to False.
        This method must be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    A class representing a member of the Stark family, inheriting from Character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Stark family member.

        :param first_name: The character's first name
        :param is_alive: Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Change the Stark character's living status to False.
        """
        self.is_alive = False
