from game.console import Console
from game.player import Player
from game.move import Move
from game.roster import Roster
from game.board import Board

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._move = None
        self._roster = Roster()
        self.keep_playing = True


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def  _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n+1}: ")
            player = Player(name)
            self._roster.add_player(player)
        self._console.write("\n")
        

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        # display the starting board
        #   --------------------
        #   Player Matt: ----, ****
        #   Player John: ----, ****
        
        

        # get next player's move
        # --------------------
        # Matt's turn:
        # What is your guess? 1111
        # 
        player = self._roster.get_current()
        text = "---------------------"
        self._console.write(text)
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess? ")
        self._console.write("\n")
        move = Move(guess)
        player.set_move(move)

        
        


    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        move = player.get_move()
        #self._board.apply(move)

        
    def do_outputs(self):

        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        if self._board.is_empty():
            winner = self._roster.get_current()
            name = winner.get_name()
            # Matt won!
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()
