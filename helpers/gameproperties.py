from enum import IntEnum
# Maze Properties
MAZEROWCOUNT = 10
MAZECOLCOUNT = 10
REDROOMFACTOR = 0.26
GREENROOMFACTOR = 0.14
BLACKROOMFACTOR = 0.06

class Direction(IntEnum):
    North = 0
    South = 1
    East = 2
    West = 3

# Player Properties
PLAYFACTORDEFAULT = 1   # this would be some sort a difficulty factor later on
PLAYERMAXHP = 100

# Enemy Properties
ENEMYGRUNTHP = 10
ENEMYHENCHMENHP = 30
ENEMYBOSSHP = 50
class EnemyType(IntEnum):
    EnemyTypeZero = 0
    EnemyTypeGrunt = 1
    EnemyTypeHenchmen = 2
    EnemyTypeBoss = 3

# Puzzle Properties
class PuzzleType(IntEnum):
    PuzzleTypeZero = 0
    PuzzleTypeEasy = 1
    PuzzleTypeMedium = 2
    PuzzleTypeHard = 3

# item Properties

# These help in bolstering player's chances of surviving a fight
SWORDMODIFIER = int(0.1 * MAZEROWCOUNT)
ARMORMODIFIER = int(0.2 * MAZECOLCOUNT)

class PlayerCollectable(IntEnum):
    NoItem = 0
    Armor = 1
    Sword = 2








