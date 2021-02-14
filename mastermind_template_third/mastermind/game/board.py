import random


class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _items (string): holds the guess, hint and num data
        guess (string): placeholder for the user information to fill in
        hint (string): stars will fill correct guesses
        equal (boolean): to compare two strings
        _num (string): this creates a random number but then changes it to a string format to compare
        names (list): to hold all the names of the players playing
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._items = ''
        self.guess = "--------"
        self.hint  = "********"
        self.equal = False
        self._num = str(random.randint(1000, 10000))
        self.names = []





    def _create_hint(self, move):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """
        guess = move.get_guess()
        self.guess += guess


        for index, letter in enumerate(guess):

            if self._num[index] == letter:
                self.hint += "x"
            elif letter in self._num:
                self.hint += "o"
            else:
                self.hint += "*"

        return self.hint

    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that
        means removing a number of stones from a pile.

        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """

        self.guess_out = move.get_guess()
        guess1 = str(self.guess_out)

        self.hint = self._create_hint(move)
        print('this is number', self._num)
        self.items = [self._num, self.guess, self.hint]




    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """

        names = self.get_names(self.names)
        text = "\n------------------------------------------"
        if len(self.hint) % 8 == 0:
            text += "\n Player " + f"{names[0]}: "
            text += (f"{self.guess[-8:-4]}: " + ", " + self.hint[-8:-4])
            text += "\n Player "  + f"{names[1]}: "
            text += (f"{self.guess[-4:]}: " + ", " + self.hint[-4:])

        else:

            text += "\n Player " + f"{names[0]}: "
            text += (f"{self.guess[-4:]}: " + ", " + self.hint[-4:])
            text += "\n Player "  + f"{names[1]}: "
            text += (f"{self.guess[-8:-4]}: " + ", " + self.hint[-8:-4])

        text += "\n------------------------------------------"
        return text

    def is_equal(self):
        """Determines if all the stones have been removed from the board.

        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """

        if self.guess[-4:] == self._num:
            self.equal = True

        return self.equal


    def get_names(self,names):
        """Determines what names were added to the game and keeps them in text format.

        Args:
            self (Board): an instance of Board.
            names (Director): a list of names from prep function.
        
        Returns:
            list: all names input to the game
        """
        self.names = names
        return names




