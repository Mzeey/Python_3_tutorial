from random import shuffle

class Deck:
    deck = []
    faceVals = ["A","J","Q","K"]
    faceScores = {"A": 11, "J":10, "Q":10, "K":10, "2": 2, "3": 3, "4": 4, "5":5, "6":6, "7":7,"8":8,"9":9, "10":10}
    def createDeck(self):
        for i in range(4):
            for card in range(2, 11):
                self.deck.append(str(card))
            for card in self.faceVals:
                self.deck.append(card)   
        self.shuffleDeck()
    
    def shuffleDeck(self):
        shuffle(self.deck)
        
    def getFaceScores(self):
        return self.faceScores
