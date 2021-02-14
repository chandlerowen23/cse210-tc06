import random

class Move:
    """A maneuver in the game. The responsibility of Move is to hold the guess information from the user.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (string): holds the users 4 digit number guess.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess

    def get_guess(self):
        """Returns the user's guess.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess
