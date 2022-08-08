from deck import Deck
class Player:
    def __init__(self, hand = [], money = 100):
        self.Hand = hand
        self.Money = money
        self.Score = 0
        self.setScore()
    def __repr__(self) -> str:
        current_hand = ""
        for card in self.Hand:
            current_hand += str(card) + " "
        return f"Current Hand: [{current_hand}]; Score: {self.Score}"

    def setScore(self):
        faceCardScore = Deck().getFaceScores()
        current_score = 0
        ace_counter = 0
        for card in self.Hand:
            current_score += faceCardScore[card]
            if card == "A": ace_counter += 1
            if current_score > 21 and ace_counter > 0: 
                current_score -= 10
                ace_counter -= 1
        self.Score = current_score
