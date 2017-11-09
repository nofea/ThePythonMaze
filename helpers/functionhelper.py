from helpers import gameproperties as gp
from random import *


def CreateRedRoom():
    enemytype = randint(gp.EnemyType.EnemyTypeGrunt, gp.EnemyType.EnemyTypeBoss)
    return enemytype

def CreateGreenRoom(): # Make puzzles here
    puzzle = randint(gp.PuzzleType.PuzzleTypeEasy, gp.PuzzleType.PuzzleTypeHard)
    return puzzle

def CreateRoomLayout(row, col, rowcount, colcount):
    layout = [True, True, True, True]
    if(row == 0):
        layout[gp.Direction.North] = False

    if(col == 0):
        layout[gp.Direction.West] = False

    if(row == rowcount - 1):
        layout[gp.Direction.South] = False

    if(col == colcount - 1):
        layout[gp.Direction.East] = False

    return(layout)

def CombatSimulator(player, enemy):
    print("\n")
    print("You come face to face with some sort of humanoid creature.")
    print("You try to avoid it and head for one of the doors.")
    print("The creature moves to block you every time you try.")
    print("Looks like it's itching for a fight, you have no other choice")

    if(player.characterItemSword == True):
        print("You unsheathe your sword")

    print("Your HP:"+str(player.characterHP))
    print("Enemy's HP:"+str(enemy.characterHP))
    print("Battling...\n")  # add loading screen

    player.characterHP = randint(int((player.characterHP - enemy.characterHP)), gp.PLAYERMAXHP)

    if(player.characterItemSword == True):
        player.characterHP += gp.SWORDMODIFIER

    if(player.characterItemArmour == True):
        player.characterHP += gp.ARMORMODIFIER

    if(player.characterHP < 0):
        print("You fought hard but, were no match to the creature's strength and cunning.")

    if(player.characterHP > gp.PLAYERMAXHP):
        player.characterHP = gp.PLAYERMAXHP

    if(player.characterHP > (gp.PLAYERMAXHP * 0.9)):
        print("You dispatch the enemy quickly and without much trouble")
    elif((player.characterHP < (gp.PLAYERMAXHP * 0.9) and player.characterHP > (gp.PLAYERMAXHP * 0.6))):
        print("The creature got in behind your guard and did some damage before you could strike the killing blow")
    elif(player.characterHP < (gp.PLAYERMAXHP * 0.6) and player.characterHP > (gp.PLAYERMAXHP * 0.1)):
        print("The creature did some serious damage and you are gravely wounded")
    else:
        print("This battle cost you heavily. You are hanging on by a thread")

    print("Your HP:"+str(player.characterHP))



def PlayerMovement(currentroom, layout):

    print("The room is empty")
    print("There are doors to the\n")
    option = 0
    choice = None

    if (layout[gp.Direction.North] == True):
        option += 1
        print(str(option)+". North\n")

    if (layout[gp.Direction.South] == True):
        option += 1
        print(str(option)+". South\n")

    if (layout[gp.Direction.East] == True):
        option += 1
        print(str(option)+". East\n")

    if (layout[gp.Direction.West] == True):
        option += 1
        print(str(option)+". West\n")

    print("Use W - North,A - West,S - South or D - East to move around the Maze.")
    choice = input("Which door do you choose to go through?\n")

    while (1):
        if ((choice == "w" or choice == "W") and layout[gp.Direction.North] == True):
            currentroom["row"] -= 1
            break
        elif ((choice == "s" or choice == "S") and layout[gp.Direction.South] == True):
            currentroom["row"] += 1
            break
        elif ((choice == "d" or choice == "D") and layout[gp.Direction.East] == True):
            currentroom["col"] += 1
            break
        elif ((choice == "a" or choice == "A") and layout[gp.Direction.West] == True):
            currentroom["col"] -= 1
            break
        else:
            print("Use W,A,S or D to move around the Maze.")
            print("If you are trying to head into a direction without a door, welcome to the concept of a wall.")
            choice = input("Please choose a valid direction\n")

    return(currentroom)

def EnemyHPFinder(enemytype):
    enemyhppool = {gp.enemytype.EnemyTypeZero: gp.ENEMYGRUNTHP,
                   gp.enemytype.EnemyTypeGrunt: gp.ENEMYHENCHMENHP,
                   gp.enemytype.EnemyTypeBoss: gp.ENEMYBOSSHP}

    return enemyhppool.get(enemytype)

def WriteConfig():
    return