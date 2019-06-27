import Deck
from Deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        # puts new player in save file
        player_name = input("Enter name: ")

        # check save files
        # boolean to see if loop was successful
        found_save = False
        f = open("blackjack_saves.txt", "r")
        for x in f:
            save = x.split("$")
            if save[0] == player_name:
                found_save = True
                self.player = Player(player_name, save[1])

        f.close()

        if found_save is False:
            self.player = Player(player_name, 50)

        self.dealer = Dealer()

    @staticmethod
    def score(hand):
        # Ace correctly evaluates whether it would be the busting card, but then continues to evaluate
        # rest of hand without reconsidering the value of the ace.
        # Must evaluate ace last.
        score = 0
        for card in hand:
            if card.rank == 'Jack' or card.rank == 'Queen' or card.rank == 'King':
                score += 10
            elif card.rank is '10' or card.rank is '9' or card.rank is '8' or card.rank is '7' or card.rank is '6' \
                    or card.rank is '5' or card.rank is '4' or card.rank is '3' or card.rank is '2':
                score += int(card.rank)
            elif card.rank == 'Ace':
                pass

        for card in hand:
            if card.rank == "Ace":
                if (score + 11) > 21:
                    score += 1
                else:
                    score += 11
            else:
                pass

        return score

    def start_game(self):
        print("Chips: " + str(self.player.chips))
        bet = input("Place your bet: ")
        bet = int(bet)
        self.player.chips -= bet

        self.player.active = True
        self.dealer.active = True
        self.player.hand = [self.deck.pull_card(), self.deck.pull_card()]
        self.dealer.hand = [self.deck.pull_card(), self.deck.pull_card()]

        print("Your hand: ")
        for card in self.player.hand:
            print(card)

        print()

        score = self.score(self.player.hand)
        print("Your total: ", score)
        if score == 21:
            print("Blackjack!")
            self.player.active = False
        print("Dealer shows: ", self.dealer.hand[1])

        while self.player.active is True:
            player_move = input("What would you like to do? (Type 'help' for options): ")
            self.player.move(player_move)

        while self.dealer.active is True:
            self.dealer.move()

        if self.dealer.active is False and self.player.active is False:
            self.end_round(self.player, self.dealer, bet)

    def end_round(self, player, dealer, bet):
        print("Dealer's hand: ")
        for card in dealer.hand:
            print(card, sep='. ', end=', ', flush=True)

        p_score = self.score(player.hand)
        d_score = self.score(dealer.hand)

        print("Dealer's score: " + str(d_score))

        p_diff = 21 - p_score
        d_diff = 21 - d_score

        if p_diff == 0:
            print("Blackjack pays out 3:2.")
            earnings = bet * 2.5
            print("You win " + str(earnings) + " chips.")
            self.player.chips += earnings
        if p_diff < 0 and d_diff < 0:
            print("You both bust.")
        elif p_diff < 0:
            print("Dealer wins.")
        elif d_diff < 0:
            print("You win!")
            earnings = bet * 2
            print("You win " + str(earnings) + " chips.")
            self.player.chips += earnings
        elif d_diff == p_diff:
            print("It's a draw.")
            self.player.chips += bet
        elif d_diff < p_diff:
            print("Dealer wins.")
        elif p_diff < d_diff:
            print("You win!")
            earnings = bet * 2
            print("You win " + str(earnings) + " chips.")
            self.player.chips += earnings

        input("Press enter to play again.")
        print("\n")
        self.start_game()


class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.active = True

    def move(self, move):
        if move == "help" or move == '?':
            print()
            print("Available moves: ")
            print("Hit")
            print("Stay")
            print("Double down")

        if move == "hit" or move == 'h':
            new_card = game.deck.pull_card()
            print(new_card)
            self.hand.append(new_card)
            score = game.score(self.hand)
            print("Your total: " + str(score))
            if score == 21:
                self.active = False
                print("Blackjack!")
            elif score > 21:
                self.active = False
                print("Bust!\n")
            else:
                pass
        if move == "stay" or move == 's':
            print("\n")
            self.active = False


class Dealer:
    def __init__(self):
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


game = Game()
game.start_game()
