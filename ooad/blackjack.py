
from enum import IntEnum
from enum import Enum
import random


class Suit(Enum):
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3
    SPADES = 4

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card(object):

    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank


class BlackJackCard(Card):

    def __init__(self, suit=None, rank=None):
        super(BlackJackCard, self).__init__(suit=suit, rank=rank)
        self.available = True


    def get_face_value(self, ace_low=True):
        if self.rank in (Rank.JACK, Rank.QUEEN, Rank.KING):
            return 10
        elif self.rank == Rank.ACE:
            if ace_low:
                return 1
            else:
                return 11
        else:
            return self.rank.value


class CardDeck(object):

    def __init__(self):
        self.num_cards_in_deck = len(Suit) * len(Rank)
        self.deck = self.build_deck()


    def build_deck(self):
        deck = list()
        for suit in Suit:
            for rank in Rank:
                bjc = BlackJackCard(suit=suit, rank=rank)
                deck.append(bjc)
        return deck


    def deal_card(self):
        found_avail_card = False
        eligible_card = None

        while not found_avail_card:
            card_idx = random.randint(0, self.num_cards_in_deck - 1)
            curr_card = self.deck[card_idx]

            if curr_card.available:
                curr_card.available = False
                found_avail_card = True
                eligible_card = curr_card
                break

        return eligible_card


class Hand(object):

    def __init__(self):
        self.cards = list()
        self.score = 0


    def add_to_hand(self, card):
        self.cards.append(card)
        self.score += card.get_face_value()


"""
Dealer also represents the House and has to hit until the House has 17 or more

NOTE:  This does not currently handle Aces with value of 11, double down, split or a stand

"""
class Dealer(object):

    def __init__(self):
        self.deck = CardDeck()
        self.house_hand = Hand()
        self.house_min_score = 17
        self.bust = False

    def deal(self):
        # house has to take a hit when its score < 17
        if self.house_hand.score < self.house_min_score:
            card = self.deck.deal_card()
            print('Dealer dealt card: {s} {r} val={v}'.format(s=card.suit, r=card.rank, v=card.get_face_value()))
            self.house_hand.add_to_hand(card)

        print('\tDealer current score: {s}'.format(s=self.house_hand.score))
        if self.house_hand.score > 21:
            self.bust = True
            print('Dealer lost')

        players_card = self.deck.deal_card()
        return players_card


"""
Player can  request a hit

"""
class Player(object):

    def __init__(self):
        self.hand = Hand()
        self.hand_max_score = 21
        self.dealer = Dealer()
        self.bust = False


    def hit(self):
        if self.hand.score < 21:
            card = self.dealer.deal()
            print('Player dealt card: {s} {r} val={v}'.format(s=card.suit, r=card.rank, v=card.get_face_value()))
            self.hand.add_to_hand(card)
        if self.hand.score > 21:
            self.bust = True
            print('Player lost')

        print('\tPlayer current score: {s}'.format(s=self.hand.score))



player = Player()

player.hit()
player.hit()
player.hit()


if not player.bust and player.hand.score > player.dealer.house_hand.score:
    print('\nPlayer won this game')
elif not player.dealer.bust and player.hand.score < player.dealer.house_hand.score:
    print('\nDealer won this game')
elif (player.dealer.bust and not player.bust):
    print('\nPlayer won this game')
elif (not player.dealer.bust and player.bust):
    print('\nDealer won this game')