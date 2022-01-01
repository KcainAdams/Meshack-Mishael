import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "of" .join((self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards= [Card(s,v)for s in ["Spades","Clubs","Hearts","Diamonds"]
                     for v in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]]

    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards)>1:
            return self.cards.pop(0)

class Hand:
    def __init__(self,dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self,card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for cards in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
    if card.value=="A"
                    has_ace=True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace & self.value >21:
            self.value -=10

    def get_value(self):
        self.calculate_value()
        return self.value