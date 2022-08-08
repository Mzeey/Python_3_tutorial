from random import shuffle

class Deck:
    deck = []
    faceVals = ["A","J","Q","K"]
    def createDeck(self):
        for i in range(4):
            for card in range(2, 11):
                self.deck.append(str(card))
            for card in self.faceVals:
                self.deck.append(card)   
        self.shuffleDeck()
    
    def shuffleDeck(self):
        shuffle(self.deck)
