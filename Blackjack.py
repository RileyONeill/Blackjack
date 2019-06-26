import Deck
from Deck import Deck


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.deck.shuffle()

    def score(self, hand):
        score = 0
        for card in hand:
            if card is 'Ace':
                
            score += card.get_value()

        return score

    def start_game(self):
        player = Player(self)
        dealer = Dealer(self)

        player.hand = [deck.pull_card(), deck.pull_card()]
        dealer.hand = [deck.pull_card(), deck.pull_card()]

        print("Your hand: ")
        for card in player.hand:
            print(card)

        print()
        print("Dealer shows: ", dealer.hand[1])

        score = self.score(player.hand)
        print("Your total: ", score)

        while player.active is True:
            player_move = input("What would you like to do? (Type 'help' for options): ")
            player.move(player_move)

        while dealer.active is True:
            dealer.move()

        if dealer.active is False and player.active is False:
            self.end_round(player, dealer)

    def end_round(self, player, dealer):

        print("Dealer's hand: ")
        for card in dealer.hand:
            print(card, sep='. ', end=', ', flush=True)

        p_score = self.score(player.hand)
        d_score = self.score(dealer.hand)

        print("Dealer's score: " + str(d_score))

        p_diff = 21 - p_score
        d_diff = 21 - d_score

        if p_diff < 0 and d_diff < 0:
            print("You both bust.")
        elif p_diff < 0:
            print("Dealer wins.")
        elif d_diff < 0:
            print("You win!")
        elif d_diff == p_diff:
            print("It's a draw.")
        elif d_diff < p_diff:
            print("Dealer wins.")
        elif p_diff < d_diff:
            print("You win!")


class Player:
    def __init__(self, game):
        self.score = 0
        self.hand = []
        self.active = True

    def move(self, move):
        if move == "help":
            print()
            print("Available moves: ")
            print("Hit")
            print("Stay")
            print("Double down")

        if move == "hit":
            new_card = game.deck.pull_card()
            print(new_card)
            self.hand.append(new_card)
            score = game.score(self.hand)
            print("Your total: " + str(score))
            if score == 21:
                self.active = False
                print("Blackjack!")
            if score > 21:
                self.active = False
                print("Bust!")
            else:
                pass
        if move == "stay":
            self.active = False


class Dealer:
    def __init__(self, game):
        self.score = 0
        self.hand = []
        self.active = True

    def move(self):
        total = game.score(self.hand)
        if total < 16:
            print("Dealer draws a card.")
            new_card = game.deck.pull_card()
            self.hand.append(new_card)
            self.move()
        if total >= 16:
            print("Dealer stays.")
            self.active = False


deck = Deck()
game = Game(deck)
game.start_game()
