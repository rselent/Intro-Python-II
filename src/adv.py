import sys, time

from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. \n\
        Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling \n\
into the darkness. Ahead to the north, a light flickers in \n\
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west \n\
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure \n\
chamber! Sadly, it has already been completely emptied by \n\
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Error speech
error = "\nPlease try to do better, adventurer. \n\
    You don't want to make this too easy for me, do you? \n\
        So let's try that again, shall we?\n\n\
            And this time, FOLLOW THE RULES...."

#
# Main
#

def main():
    # introduction
    print( "\nWelcome to your new reality, adventurer. \n\
        I am here to make things interesting for you, and... \n\
            you are here to entertain me.... hahahahahaHAAHAHAHAHA\n\n")

    # Make a new player object that is currently in the 'outside' room.
    playerName = input( "What is your name, adventurer, should I choose to \
        humiliate you with it? ")    
    adventurer = Player( playerName, room[ 'outside'])

    while 1:
        # prints current room name/description for every game loop
        print( "\nYour current location: ")
        print( adventurer.loc.printDescription)

        userInput = input( "\nMake your decision, adventurer... what do you want to do: ").lower

        # error/repeat on leading space
        if userInput[0] == ' ':
            print( error)

        # if input is 1 character in length: quit, move, or error/repeat
        if len( userInput) < 2:
            if userInput == "q":
                print( "\nFarewell, adventurer. Until next time...")
                time.sleep( 2)
                sys.exit( 0)
            elif userInput in ["n", "e", "s", "w"]:
                adventurer.loc = adventurer.move_to( userInput, adventurer.loc)
            else:
                print( error)

        # if input is greater than 1 character in length:
        # check if multiple words, then check & execute accordingly, or error/repeat
        if len( userInput) > 1:
            inputSplit = str( userInput).split
            if inputSplit[0] == "move":
                if inputSplit[1] in ["n", "e", "s", "w", 
                                 "north", "east", 
                                 "south", "west"]:
                    adventurer.loc = adventurer.move_to( userInput, adventurer.loc)
                else:
                    print( f"Oh, {Player.name}, look at what you've done now. \n\
                        You've gone and forgotten your directions! \n\
                            Now we have to start allllllll the way back from the BEGINNING!\n\n\
                                And to think, you were beginning to show so much promise, too...\n\n"
                    )
            
            #["move", "take", "use", "drop"]:
            #    ...


if __name__ == "__main__":
    main()



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
