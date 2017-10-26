from enum import IntEnum
# Maze Properties
MAZESIZE = 50   # assumption is a square maze of the order MAZESIZE
REDROOMFACTOR = 0.26
GREENROOMFACTOR = 0.14
BLACKROOMFACTOR = 0.06

class Direction(IntEnum):
    North = 0
    South = 1
    East = 2
    West = 3

# Player Properties
PLAYFACTORDEFAULT = 1
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








