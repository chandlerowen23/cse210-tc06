from game.console import Console
from game.killer import Killer
from game.guesser import Guesser

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        Killer (Killer): An instance of the class of objects known as killer.
        guesser (Guesser): An instance of the class of objects known as Guesser.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.killer = Killer()
        self.keep_playing = True
        self.guesser = Guesser()
        self.fails = 0
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        message = self.guesser.get_hint()
        self.console.write(message)
        self.killer.get_fails(self.fails)
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

            if self.fails == 4:
                self.keep_playing = False


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """


        self.letter = self.console.read_word("Guess a letter [a-z]: ")



    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """

        hint = self.guesser.do_guess(self.letter)
        self.console.write(hint)
        self.fails = self.guesser.get_back_fails()


        
    def do_outputs(self):

        self.killer.get_fails(self.fails)
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
