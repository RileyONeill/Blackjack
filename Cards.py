
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if rank is "Ace":
            self.value = 11

        elif rank is "King" or rank is "Queen" or rank is "Jack":
            self.value = 10

        else:
            self.value = int(rank)

    def __repr__(self):
        return "%s of %s" % (self.rank, self.suit)

