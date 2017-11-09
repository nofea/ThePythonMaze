class Character:
    characterHP = 0
    characterItemSword = False
    characterItemArmour = False
    characterItemHealthPotion = 0

    def __init__(self, characterHP, characterItemSword, characterItemArmour, characterItemHealthPotion):
        self.characterHP = characterHP
        self.characterItemSword = characterItemSword
        self.characterItemArmour = characterItemArmour
        self.characterItemHealthPotion = characterItemHealthPotion