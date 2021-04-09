"""
The deck is divided evenly, with each player receving 26 cards, dealt one at a time,face down.
Anyone may deal first. Each player places his stack of cards face down, in front of him/her.

The Play:

Each player turns up a card at the same time and the player with the higher card takes both cards and puts them,
face down, on the bottom of his stack.

If the cards are the sam rank, it is WAR. Each player turns up three cards face down and one card face up.
The player with the higher cards takes both piles(six cards). If the turned-up cards are again the same rank, 
each player places another card face down and turns another card face up. 
The player with the hihger card takes all 10 cards and so on...
"""
from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A '.split()


class Deck:
    """
    This is the Deck class. This object will create a deck of cards to intiate play.
    You can then use this Deck list of cards to split in half and give to the players. 
    It will use SUITE and RANKS to create the deck. It should also have a method for splitting/cutting the deck in half,
    and shuffle the deck.

    """

    def __init__(self, card=[]):
        cards = list()
        for x in SUITE:
            for y in RANKS:
                cards.append(y+x)
        self.cards = cards

    def split(self):
        shuffle(self.cards)
        q1 = self.cards[:26]
        shuffle(q1)
        q2 = self.cards[26:]
        shuffle(q2)
        return [q1, q2]


"""
    Each player has a Hand, and can add or remove cards from that hand. 
    There should be an add and remove card method here.
    """


class Hand:
    def __init__(self, card_set):
        self.card_set = card_set

    def add(self, card):
        self.card_set.append(card)

    def remove(self):
        return self.card_set.pop(0)

    def get_card_set(self):
        return self.card_set

    def set_card_set(self, card_set):
        self.card_set = card_set


"""
    The Player class takes in a name and an instance of a Hand class objekt. 
    The player can then play cards and check if they still have cards.
    """


class Player:
    def __init__(self, name, card_set):
        self.name = name
        self.hand = Hand(card_set)

    def card_drawn(self, card):
        # print(self.hand.card_set)
        #print("card turned is ",card)
        card = card[:-1]
        if card == 'J':
            card = 11
        elif card == 'Q':
            card = 12
        elif card == 'K':
            card = 13
        elif card == 'A':
            card = 14
        # print(card)
        return int(card)

    def get_card(self):
        return self.hand.remove()

    def card_left(self):
        pass

    def get_hand(self):
        return self.hand

    def set_hand(self, hand):
        self.hand = hand

    
def game_play(names: []):
    print("Welcome to War, lets begin...")
    deck = Deck()
    card_sets = deck.split()

    player1 = Player(names[0], card_sets[0])
    player2 = Player(names[1], card_sets[1])

    player1_card_count = len(card_sets[0])
    player2_card_count = len(card_sets[1])

    print(player1.name, player1.hand.card_set)
    print(player2.name, player2.hand.card_set)
    n = 0
    while (player1_card_count < 52 and player2_card_count < 52 and n < 10000):
        n += 1
        print("Round ", n)
        # if player1_card_count
        card1 = player1.get_card()
        card2 = player2.get_card()
        player1_card_count -= 1
        player2_card_count -= 1

        print("{} turned card: {} and {} turned this card {} ".format(
            names[0], card1, names[1], card2))

        if player1.card_drawn(card1) == player2.card_drawn(card2):
            print("Its war...")
            war_cards = [card1, card2]
            war = True

            while war and player1_card_count >= 2 and player2_card_count >= 2:
                war = False
                card3 = player1.get_card()
                card4 = player2.get_card()
                card5 = player1.get_card()
                card6 = player2.get_card()
                player1_card_count -= 2
                player2_card_count -= 2

                for i in [card3, card4, card5, card6]:
                    war_cards.append(i)

                if player1.card_drawn(card5) == player2.card_drawn(card6):
                    print("War again...")
                    war = True
                    continue

                elif player1.card_drawn(card5) > player2.card_drawn(card6):
                    for i in war_cards:
                        player1.hand.add(i)
                    player1_card_count += len(war_cards)
                    print("{} win this war... total cards {}".format(
                        player1.name, player1_card_count))
                    war_cards = []
                else:
                    for i in war_cards:
                        player2.hand.add(i)
                    player2_card_count += len(war_cards)
                    print("{} win this war... total cards {}".format(
                        player2.name, player2_card_count))
                    war_cards = []

            if player1_card_count < 3:
                for i in war_cards:
                    player2.hand.add(i)
                player2_card_count += len(war_cards)

            if player2_card_count < 3:
                for i in war_cards:
                    player1.hand.add(i)
                player1_card_count += len(war_cards)

        elif player1.card_drawn(card1) > player2.card_drawn(card2):
            player1.hand.add(card1)
            player1.hand.add(card2)
            player1_card_count += 2
            print("player1_count {} and player2_count {}".format(
                player1_card_count, player2_card_count))
        else:
            player2.hand.add(card1)
            player2.hand.add(card2)
            player2_card_count += 2
            print("player1_count {} and player2_count {}".format(
                player1_card_count, player2_card_count))

    if(player1_card_count == 52):
        print(player1.name, " won!!")
        print("{} : {}".format(player1.name, player1_card_count))
        print("{} : {}".format(player2.name, player2_card_count))
    elif(player2_card_count == 52):
        print(player2.name, " won!!")
        print("{} : {}".format(player1.name, player1_card_count))
        print("{} : {}".format(player2.name, player2_card_count))
    else:
        print("Game terminated...taking too much time")
        print("{} : {}".format(player1.name, player1_card_count))
        print("{} : {}".format(player2.name, player2_card_count))




game_play(['Shalini', 'Ali'])
