from deck import Deck

class App:
    deck = Deck()
    
    def start(self):
        self.deck.createDeck()
        print(self.deck.deck)
    
app = App()
app.start()