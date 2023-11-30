# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hello Player! Welcome to the Quiz Game. "

    e "In this game, you will have to answer questions that are displayed on the screen in order to earn points. "

    e "As you answer more questions correctly, the difficulty will become harder, and the randomness of the questions will increase. "

    e "Good luck!"

    # This ends the game.

    return
