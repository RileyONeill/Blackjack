import Cards


class Deck:

    def __init__(self):
        self.deck = []
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.create_deck()

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                new_card = Cards.Card(rank, suit)
                self.deck.append(new_card)


deck = Deck()
