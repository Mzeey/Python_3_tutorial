from random import randint
from house import House
from player import Player
from deck import Deck
from message import Message

class App:
    SCORE_LIMIT = 21
    MESSAGE = Message()
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.createDeck()
        first_hand = [self.deck.deck.pop(), self.deck.deck.pop()]
        second_hand =[self.deck.deck.pop(), self.deck.deck.pop()]
        self.Player_1, self.House = Player(first_hand), House(second_hand)
        
    def start(self):
        while True:
            self.startRound()
            bet = int(input(self.MESSAGE.PLACE_BET))
            self.Player_1.bet(bet)
            print(self.Player_1)
            if self.Player_1.checkBlackJack():
                if self.House.checkBlackJack():
                    self.Player_1.draw()
                else:
                    self.Player_1.win(True)
            else:  
                self.playerDraw()
                self.houseDraw()
                self.checkWinner()
            print(f"{self.MESSAGE.ROUND_ENDED}{self.Player_1.Money}")
            action = input(self.MESSAGE.CONTINUE_PLAYING)
            if action == "y":
                print(self.MESSAGE.STARTING_ROUND)
            else:
                print(f"{self.MESSAGE.GAME_OVER}{self.Player_1.Money}")
                break
            
    def startRound(self):
        if len(self.deck.deck) > 20:
                self.deck = Deck()
                self.deck.createDeck()
        self.Player_1.play([self.deck.deck.pop(), self.deck.deck.pop()])
        self.House.play([self.deck.deck.pop(), self.deck.deck.pop()])
        
 
    def playerDraw(self):
        while self.Player_1.Score < self.SCORE_LIMIT:
            action = input(self.MESSAGE.DRAW_CARD)
            if action == "y":
                self.Player_1.hitCard(self.deck.deck.pop())
                print(f"You -> {self.Player_1}")
                print(f"House -> {self.House}")
            else:
                break
    
    def houseDraw(self):
        while self.House.Score < self.SCORE_LIMIT:
            action = randint(0,1)
            if action == 1:
                self.House.hitCard(self.deck.deck.pop())
            else:
                break
    
    def checkWinner(self):
        if self.Player_1.Score > 21:
            if self.House.Score > 21:
                self.Player_1.draw()
            else:
                self.Player_1.win(False)
        elif self.Player_1.Score > self.House.Score:
            self.Player_1.win(True)
        elif self.Player_1.Score == self.House.Score:
            self.Player_1.draw()
        else:
            if self.House.Score > 21:
                self.Player_1.win(True)
app = App()
app.start()