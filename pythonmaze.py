import gameproperties as gp
import functionhelper as fh
import pdb # debug

print("Welcome to the MAZE")
print("Now, let's see you get out")
redrooms, greenrooms, blackrooms, mazeentry, mazeexit = fh.InitMaze()
print("\n\n")
currentroom = mazeentry

while(currentroom is not mazeexit):
    print("You are in a room")
    layout = fh.CreateRoomLayout(row=currentroom.get('row'), col=currentroom.get('col'))
    if(currentroom == mazeexit):
        print("You see the exit from this accursed maze. You run to it and you are finally out")
        print("Thank you for playing The Maze")
        break
    elif(currentroom == mazeentry):
        currentroom = fh.PlayerMovement(currentroom=currentroom, layout=layout)
    else:
        found = False
        for red in redrooms:
            if(currentroom == red):
                enemy = fh.CreateRedRoom()
                # do combat here
                currentroom = fh.PlayerMovement(currentroom=currentroom, layout=layout)
                found = True
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
                    print("You hear a loud click sound from right beneath you and realise, too late, that it's a trap door.")
                    print("You fall through and land, hard, on a stone surface somewhere below the maze.")
                    print("After wandering around for a bit, you see a ladder that heads up and out of this place.")
                    print("You climb out of that infernal place only to find yourself back at the maze's entrance.")
                    print("You, now, have to start all over again.\n\n")
                    currentroom = mazeentry
                    break







