import gameproperties as gp
from random import *

def InitMaze():
    # read historic data from config file here and determine a factor of how the players skill. Failing this, just use a default value
    playfactor = gp.PLAYFACTORDEFAULT

    if(playfactor != gp.PLAYFACTORDEFAULT):
        return("oops")

    redroomsmax = int(gp.MAZESIZE * gp.MAZESIZE * gp.REDROOMFACTOR)
    greenroomsmax = int(gp.MAZESIZE * gp.MAZESIZE * gp.GREENROOMFACTOR)
    blackroomsmax = int(gp.MAZESIZE * gp.MAZESIZE * gp.BLACKROOMFACTOR)

    redrooms = [] #enemypresence
    greenrooms = [] #puzzles
    blackrooms = [] #traps
    index = 0
    mazeentry = {}
    mazeexit = {}
    redroom = {}
    greenroom = {}
    blackroom = {}

    while(1):
        redroom = {'row': randint(1, gp.MAZESIZE), 'col': randint(1, gp.MAZESIZE)}
        greenroom = {'row': randint(1, gp.MAZESIZE), 'col': randint(1, gp.MAZESIZE)}
        blackroom = {'row': randint(1, gp.MAZESIZE), 'col': randint(1, gp.MAZESIZE)}
        found = False

        for red in redrooms:
            if((redroom.get('row') == red.get('row') and redroom.get('col') == red.get('col')) or
                   (greenroom.get('row') == red.get('row') and greenroom.get('col') == red.get('col')) or
                   (blackroom.get('row') == red.get('row') and blackroom.get('col') == red.get('col'))):
                found = True
                break

        if(found == False):
            for green in greenrooms:
                if((redroom.get('row') == green.get('row') and redroom.get('col') == green.get('col')) or
                           (greenroom.get('row') == green.get('row') and greenroom.get('col') == green.get('col')) or
                       (blackroom.get('row') == green.get('row') and blackroom.get('col') == green.get('col'))):
                    found = True
                    break

        if(found == False):
            for black in blackrooms:
                if((redroom.get('row') == black.get('row') and redroom.get('col') == black.get('col')) or
                       (greenroom.get('row') == black.get('row') and greenroom.get('col') == black.get('col')) or
                       (blackroom.get('row') == black.get('row') and blackroom.get('col') == black.get('col'))):
                    found = True
                    break


        if(found == False):
            if(index < blackroomsmax):
                redrooms.append(redroom)
                greenrooms.append(greenroom)
                blackrooms.append(blackroom)

            elif(index < greenroomsmax):
                redrooms.append(redroom)
                greenrooms.append(greenroom)

            elif(index < redroomsmax):
                redrooms.append(redroom)

            else:
                edge = randint(gp.Direction.North, gp.Direction.West)
                if(edge == gp.Direction.North):
                    mazeentry = {'row': 0, 'col': redroom.get('col')}
                    mazeexit = {'row': (gp.MAZESIZE - 1), 'col': redroom.get('row')}

                elif(edge == gp.Direction.South):
                    mazeentry = {'row': (gp.MAZESIZE - 1), 'col': redroom.get('col')}
                    mazeexit = {'row': 0, 'col': redroom.get('row')}

                elif(edge == gp.Direction.East):
                    mazeentry = {'row': redroom.get('row'), 'col': (gp.MAZESIZE - 1)}
                    mazeexit = {'row': redroom.get('col'), 'col': 0}

                else:
                    mazeentry = {'row': redroom.get('row'), 'col': 0}
                    mazeexit = {'row': redroom.get('col'), 'col': (gp.MAZESIZE - 1)}

                break

            index += 1
    return(redrooms, greenrooms, blackrooms, mazeentry, mazeexit)

def CreateRedRoom():
    enemy = randint(gp.EnemyType.EnemyTypeGrunt, gp.EnemyType.EnemyTypeBoss)
    return enemy

def CreateGreenRoom(): # Make puzzles here
    puzzle = randint(gp.PuzzleType.PuzzleTypeEasy, gp.PuzzleType.PuzzleTypeHard)
    return puzzle

def CreateRoomLayout(row, col):
    layout = [True, True, True, True]
    if(row == 0):
        layout[gp.Direction.North] = False

    if(col == 0):
        layout[gp.Direction.West] = False

    if(row == gp.MAZESIZE - 1):
        layout[gp.Direction.South] = False

    if(col == gp.MAZESIZE - 1):
        layout[gp.Direction.East] = False

    return(layout)

def CombatSimulator(enemy,player,combatmodifier):
    return enemy, player

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


def WriteConfig():
    return