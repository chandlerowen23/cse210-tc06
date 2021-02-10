import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self.num1 = 0
        self.num2 = 0
        self._prepare()

    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
    
    def is_empty(self):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        pass

    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 
        pass

    def _prepare(self):
        """Sets up the board with a random number of piles containing a random 
        number of stones.
        
        Args:
            self (Board): an instance of Board.
        """
        self.num1 = random.randint(1000, 9999)
        self.num2 = random.randint(1000, 9999)

        
