import random



class Board():
    """creates board with random number of piles and stones
    
    Attributes:
        _piles is list of piles and data contained in them.
        _prepare is a private function to call the prepare function and set stones per pile
    """
    def __init__(self):
        # Private Attribute
        self._piles = []
        self._prepare()

    # Private function
    def _prepare(self):
        piles = random.randint(2,5)
        for i in range(piles):
            stones = random.randint(1,9)
            self._piles.append(stones)

    # Public Function
    def apply(self, move):
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)
    
    # Public Function
    def is_empty(self):
        empty = [0]*len(self._piles)
        return self._piles == empty
    
    # Public Function
    def to_string(self):
        #Text is called from the director to display on the console
        #the text variable must be added to in order to print all the needed information
        text = "\n--------------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "0" * stones)
        text += "\n--------------------"
        return text

