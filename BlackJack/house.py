from player import Player

class House(Player):
    def __repr__(self) -> str:
        current_card = ""
        for card in range(len(self.Hand)):
            if card == len(self.Hand) -1:
                current_card += f"{self.Hand[card]} "
            else:
                current_card += "* "
        return f"Hand: [{current_card}]"
    def showHouse(self):
        return super().__repr__()