import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f"{self.number} of {self.suit}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self,other):
        return self.number<other.number

    def __gt__(self,other):
        return self.number>other.number

    def __eq__(self,other):
        return self.number==other.number


class Deck:
    def __init__ (self, suits, numbers):
        self.stack = []
        for x in suits:
            for n in numbers:
                self.stack.append (Card (n,x))
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.stack)
    def draw(self):
        return self.stack.pop(0)
    def len (self):
        return len(d.stack)


class Player: 
    def __init__ (self,name):
        self.winnings = []
        self.hand = [] 
        self.name = name
    def draw (self,deck, n):
        cards = []
        for _ in range(n):
            cards.append(deck.draw())
        self.hand += cards
    def reload (self):
        hand_empty =len (self.hand) == 0
        winnings_empty = len(self.winnings) == 0
        if hand_empty and winnings_empty:
            return None
        elif hand_empty:
            random.shuffle (self.winnings)
            self.hand.extend(self.winnings)
            self.winnings = []
        return self.hand.pop(0)


def decider (player1card, player2card):
    if not player1card:
        return "player 2 Wins!"
    if not player2card:
        return "player 1 wins!"
    if player1card > player2card:
        return "winner"
    if player1card <  player2card:
        return "loser"
    if player1card == player2card:
        return "we both suck"


## each iteration of the loop represents one turn of the game.
def game(player1, player2):
    pot = []
    while True:
        player1card = player1.reload()
        player2card = player2.reload()
        pot += [player1card, player2card] 

        if player1card is None:
            print ("player 2 wins!")
            break
        elif player2card is  None:
            print ("player 1 wins!")
            break
        res = decider(player1card, player2card)
        if res == "winner":
            player1.winnings += pot
            pot =[]
        elif res  == "loser":
            player2.winnings += pot
            pot = []
        else:
            pot += [
                player1.reload(),
                player1.reload(),
                player2.reload(),
                player2.reload(),
            ]
                
        print (f"\nplayer1: {player1card}\t player2: {player2card}\n{res}")
    print (player1.winnings, player2.winnings)


def main():
    d = Deck(["clubs", "spades", "hearts", "diamonds"], list(range(2,15)))

    player1 = Player ("player1")
    player2 = Player ("player2")
    
    d.shuffle()
    player1.draw(d,26)
    player2.draw(d,26)

    game(player1, player2)

if __name__ == '__main__':
    main()

        
