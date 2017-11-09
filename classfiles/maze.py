from helpers import gameproperties as gp
from random import *

class Maze:
    rowcount = 0
    colcount = 0

    def __int__(self, rowcount, colcount):
        self.rowcount = rowcount
        self.colcount = colcount

    def InitMaze(self, mazedatacontainer):
        # read historic data from config file here and determine a factor of how the players skill. Failing this, just use a default value

        mazesize = self.rowcount * self.colcount
        redroomsmax = int(mazesize * mazedatacontainer.get('redroomfactor'))
        greenroomsmax = int(mazesize * mazedatacontainer.get('greenroomfactor'))
        blackroomsmax = int(mazesize * mazedatacontainer.get('blackroomfactor'))

        redrooms = []  # enemypresence
        greenrooms = []  # puzzles
        blackrooms = []  # traps
        index = 0
        mazeentry = {}
        mazeexit = {}
        redroom = {}
        greenroom = {}
        blackroom = {}

        while (1):
            redroom = {'row': randint(1, self.rowcount), 'col': randint(1, self.colcount)}
            greenroom = {'row': randint(1, self.rowcount), 'col': randint(1, self.colcount)}
            blackroom = {'row': randint(1, self.rowcount), 'col': randint(1, self.colcount)}
            found = False

            for red in redrooms:
                if ((redroom.get('row') == red.get('row') and redroom.get('col') == red.get('col')) or
                        (greenroom.get('row') == red.get('row') and greenroom.get('col') == red.get('col')) or
                        (blackroom.get('row') == red.get('row') and blackroom.get('col') == red.get('col'))):
                    found = True
                    break

            if (found == False):
                for green in greenrooms:
                    if ((redroom.get('row') == green.get('row') and redroom.get('col') == green.get('col')) or
                            (greenroom.get('row') == green.get('row') and greenroom.get('col') == green.get('col')) or
                            (blackroom.get('row') == green.get('row') and blackroom.get('col') == green.get('col'))):
                        found = True
                        break

            if (found == False):
                for black in blackrooms:
                    if ((redroom.get('row') == black.get('row') and redroom.get('col') == black.get('col')) or
                            (greenroom.get('row') == black.get('row') and greenroom.get('col') == black.get('col')) or
                            (blackroom.get('row') == black.get('row') and blackroom.get('col') == black.get('col'))):
                        found = True
                        break

            if (found == False):
                if (index < blackroomsmax):
                    redrooms.append(redroom)
                    greenrooms.append(greenroom)
                    blackrooms.append(blackroom)

                elif (index < greenroomsmax):
                    redrooms.append(redroom)
                    greenrooms.append(greenroom)

                elif (index < redroomsmax):
                    redrooms.append(redroom)

                else:
                    edge = randint(gp.Direction.North, gp.Direction.West)
                    if (edge == gp.Direction.North):
                        mazeentry = {'row': 0, 'col': redroom.get('col')}
                        mazeexit = {'row': (self.rowcount - 1), 'col': redroom.get('row')}

                    elif (edge == gp.Direction.South):
                        mazeentry = {'row': (self.rowcount - 1), 'col': redroom.get('col')}
                        mazeexit = {'row': 0, 'col': redroom.get('row')}

                    elif (edge == gp.Direction.East):
                        mazeentry = {'row': redroom.get('row'), 'col': (self.colcount - 1)}
                        mazeexit = {'row': redroom.get('col'), 'col': 0}

                    else:
                        mazeentry = {'row': redroom.get('row'), 'col': 0}
                        mazeexit = {'row': redroom.get('col'), 'col': (self.colcount - 1)}

                    break

                index += 1
        return (redrooms, greenrooms, blackrooms, mazeentry, mazeexit)
