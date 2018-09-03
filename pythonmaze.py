#!/usr/bin/env python3
from helpers import gameproperties as gp
from helpers import functionhelper as fh
from classfiles import maze
from classfiles import enemy
from classfiles import player

print("Welcome to the MAZE")
print("Now, let's see you get out")
fh.pressentertocontinue()
mz = maze.Maze()
mz.rowcount = gp.MAZEROWCOUNT
mz.colcount = gp.MAZECOLCOUNT

playerItems = {gp.PlayerCollectable.Armor: False, gp.PlayerCollectable.Sword: False, gp.PlayerCollectable.HealthPortion: gp.PLAYERHEALTHPORTION}
ply = player.Player(characterHP=gp.PLAYERMAXHP, characterItems=playerItems)
mazedatacontainer = {'redroomfactor': gp.REDROOMFACTOR, 'greenroomfactor': gp.GREENROOMFACTOR, 'blackroomfactor': gp.BLACKROOMFACTOR}
redrooms, greenrooms, blackrooms, mazeentry, mazeexit = mz.createmaze(mazedatacontainer)

print("\n\n")
ply.currentroom = {'row': mazeentry.get('row'), 'col': mazeentry.get('col')}

playerdeath = False
while(ply.currentroom is not mazeexit):
    fh.separator()
    print("You are in a room")
    layout = fh.createroomlayout(row=ply.currentroom.get('row'), col=ply.currentroom.get('col'), rowcount=mz.rowcount, colcount=mz.colcount)
    if(ply.currentroom.get('row') == mazeexit.get('row') and ply.currentroom.get('col') == mazeexit.get('col')):
        print("You see the exit from this accursed maze. You run to it and you are finally out")
        fh.pressentertocontinue()
        print("Thank you for playing The Maze")
        break
    elif(ply.currentroom.get('row') == mazeentry.get('row') and ply.currentroom.get('col') == mazeentry.get('col')):
        ply.currentroom = fh.playermovement(currentroom=ply.currentroom, layout=layout)
    else:
        found = False
        for red in redrooms:
            if(ply.currentroom == red):
                enemytype = fh.createredroom()
                enemyItems = {gp.PlayerCollectable.Armor: False, gp.PlayerCollectable.Sword: False, gp.PlayerCollectable.HealthPortion: 0}
                enmy = enemy.Enemy(characterHP=fh.enemyhpfinder(enemytype=enemytype), characterItems=enemyItems)
                enmy.enemytype = enemytype
                fh.combatsimulator(player=ply, enemy=enmy)

                if(ply.characterHP <= 0):
                    playerdeath = True
                    break
                else:
                    del enmy
                    fh.separator()

                ply.currentroom = fh.playermovement(currentroom=ply.currentroom, layout=layout)
                found = True
                break

        if(playerdeath == True):
            print("GAME OVER")
            break

        if(found == False):
            for green in greenrooms:
                if(ply.currentroom == green):
                    puzzle = fh.creategreenroom()
                    # do puzzles here
                    ply.currentroom = fh.playermovement(currentroom=ply.currentroom, layout=layout)
                    found = True
                    break

        if(found == False):
            for black in blackrooms:
                if(ply.currentroom == black):
                    print("Thinking that it's empty you walk to the centre of the room.")
                    print("You hear a loud click from right beneath you and realise, too late, that it's a trap door.")
                    print("You fall through and land, hard, on a stone surface somewhere below the maze.")
                    print("After wandering around for a bit, you see a ladder that heads up and out.")
                    print("You climb out of that infernal place only to find yourself back at the maze's entrance.")
                    print("You, now, have to start all over again.\n\n")
                    fh.pressentertocontinue()
                    ply.currentroom = {'row': mazeentry.get('row'), 'col': mazeentry.get('col')}
                    break


        if(found == False):
            ply.currentroom = fh.playermovement(currentroom=ply.currentroom, layout=layout)




