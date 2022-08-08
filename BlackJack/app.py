from random import randint
from xmlrpc.client import FastParser
from house import House
from player import Player
from deck import Deck

class App:
    deck = Deck()
    def start(self):
        self.deck.createDeck()
        first_hand = [self.deck.deck.pop(), self.deck.deck.pop()]
        second_hand =[self.deck.deck.pop(), self.deck.deck.pop()]
        self.Player_1, self.House = Player(first_hand), House(second_hand)
        
        while True:
            if len(self.deck.deck) > 20:
                self.deck = Deck()
                self.deck.createDeck()
            self.Player_1.play([self.deck.deck.pop(), self.deck.deck.pop()])
            self.House.play([self.deck.deck.pop(), self.deck.deck.pop()])
        
            Bet = int(input("Please enter your bet: "))
            self.Player_1.bet(Bet)
            if self.Player_1.checkBlackJack():
                if self.House.checkBlackJack():
                    self.Player_1.draw()
                else:
                    self.Player_1.win(True)
            else:  
                while self.Player_1.Score < 21:
                    action = input("do you want another card(y/n)?: ")
                    if action == "y":
                        self.Player_1.hitCard(self.deck.deck.pop())
                        print(f"You -> {self.Player_1}")
                        print(f"House -> {self.House}")
                    else:
                        break
                    
                while self.House.Score < 21:
                    action = randint(0,1)
                    if action == 1:
                        self.House.hitCard(self.deck.deck.pop())
                        print(f"House -> {self.House.showHouse()}")
                    else:
                        break
                    
                #Checking winner
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
            print(self.Player_1.Money)
                
app = App()
app.start()
print(app.House.showHouse(), app.Player_1)