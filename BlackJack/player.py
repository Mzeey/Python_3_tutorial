from deck import Deck
class Player:
    def __init__(self, hand = [], money = 100):
        self.Hand = hand
        self.Money = money
        self.Score = 0
        self.Bet = 0
        self.setScore()
    def __repr__(self) -> str:
        current_hand = ""
        for card in self.Hand:
            current_hand += str(card) + " "
        return f"Current Hand: [{current_hand}]; Score: {self.Score}"

    def __checkBlackJack(self):
        isBlackJack = False
        if self.Score == 21 and len(self.Hand) == 2:
            isBlackJack = True
        return isBlackJack

    def setScore(self):
        faceCardScore = Deck().getFaceScores()
        current_score = 0
        ace_counter = 0
        for card in self.Hand:
            current_score += faceCardScore[card]
            if card == "A": 
                ace_counter += 1
            if current_score > 21 and ace_counter > 0: 
                current_score -= 10
                ace_counter -= 1
        self.Score = current_score
    
    def hitCard(self, card):
        self.Hand.append(card)
        self.setScore()
    
    def play(self):
        self.__init__()
    
    def bet(self, ammount):
        self.Money -= ammount
        self.Bet = ammount
        
    def win(self, has_won):
        DOUBLE_BET = 2
        BLACKJACK_BET = 2.5
        isBlackJack = self.__checkBlackJack()
        if has_won == True:
            if isBlackJack:
                self.Money += round(self.Bet * BLACKJACK_BET)
            else:
                self.Money += self.Bet * DOUBLE_BET
        self.Bet = 0

player = Player(["3", "7", "5"])
print(player)

player.play()
player.hitCard("A")
player.hitCard("K")

player.bet(50)
player.win(False)
print(player.Money)
print(player)

