#!/usr/bin/env python3
from helpers import gameproperties as gp
from helpers import functionhelper as fh
from classfiles import maze
from classfiles import enemy
from classfiles import player

print("Welcome to the MAZE")
print("Now, let's see you get out")
mz = maze.Maze()
mz.rowcount = gp.MAZEROWCOUNT
mz.colcount = gp.MAZECOLCOUNT
ply = player.Player(characterHP=gp.PLAYERMAXHP, characterItemSword=False, characterItemArmour=False, characterItemHealthPotion=False)
mazedatacontainer = {'redroomfactor': gp.REDROOMFACTOR, 'greenroomfactor': gp.GREENROOMFACTOR, 'blackroomfactor': gp.BLACKROOMFACTOR}
redrooms, greenrooms, blackrooms, mazeentry, mazeexit = mz.InitMaze(mazedatacontainer)

print("\n\n")
currentroom = {'row': mazeentry.get('row'), 'col': mazeentry.get('col')}

playerdeath = False
while(currentroom is not mazeexit):
    print("You are in a room")
    layout = fh.CreateRoomLayout(row=currentroom.get('row'), col=currentroom.get('col'), rowcount=mz.rowcount, colcount=mz.colcount)
    if(currentroom.get('row') == mazeexit.get('row') and currentroom.get('col') == mazeexit.get('col')):
        print("You see the exit from this accursed maze. You run to it and you are finally out")
        print("Thank you for playing The Maze")
        break
    elif(currentroom.get('row') == mazeentry.get('row') and currentroom.get('col') == mazeentry.get('col')):
        currentroom = fh.PlayerMovement(currentroom=currentroom, layout=layout)
    else:
        found = False
        for red in redrooms:
            if(currentroom == red):
                enemytype = fh.CreateRedRoom()
                enmy = enemy.Enemy(characterHP=fh.EnemyHPFinder(enemytype), characterItemSword=False, characterItemArmour=False, characterItemHealthPotion=False, enemytype=enemytype)
                fh.CombatSimulator(player=ply, enemy=enmy)

                if(ply.characterHP <= 0):
                    playerdeath = True
                    break
                else:
                    del enmy

                currentroom = fh.PlayerMovement(currentroom=currentroom, layout=layout)
                found = True
                break

        if(playerdeath == True):
            print("GAME OVER")
            break

        if(found == False):
            for green in greenrooms:
                if(currentroom == green):
                    puzzle = fh.CreateGreenRoom()
                    # do puzzles here
                    currentroom = fh.PlayerMovement(currentroom=currentroom, layout=layout)
                    found = True
                    break

        if(found == False):
            for black in blackrooms:
                if(currentroom == black):
                    print("Thinking that it's empty you walk to the centre of the room.")
                    print("You hear a loud click from right beneath you and realise, too late, that it's a trap door.")
                    print("You fall through and land, hard, on a stone surface somewhere below the maze.")
                    print("After wandering around for a bit, you see a ladder that heads up and out.")
                    print("You climb out of that infernal place only to find yourself back at the maze's entrance.")
                    print("You, now, have to start all over again.\n\n")
                    currentroom = {'row': mazeentry.get('row'), 'col': mazeentry.get('col')}
                    break


        if(found == False):
            currentroom = fh.PlayerMovement(currentroom=currentroom, layout=layout)




