from classfiles.character import Character
from helpers import gameproperties as gp

class Enemy(Character):
    enemytype = gp.EnemyType.EnemyTypeZero

    def __init__(self, enemytype):
        self.enemytype = enemytype
