from helpers import gameproperties as gp
class Character:
    characterHP = 0
    characterItemSword = False
    characterItemArmour = False
    characterItemHealthPotion = 0
    currentroom = {'row': None, 'col': None}

    def __init__(self, characterHP, characterItems):
        self.characterHP = characterHP
        self.characterItemSword = characterItems[gp.PlayerCollectable.Sword]
        self.characterItemArmour = characterItems[gp.PlayerCollectable.Armor]
        self.characterItemHealthPotion = characterItems[gp.PlayerCollectable.HealthPortion]
        