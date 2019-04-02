# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define pig1 = Character("First Little Piggy")
define pig2 = Character("Second Little Piggy")
define pig3 = Character("Third Little Piggy")
define wolf = Character("Big Bad Wolf")

# The game starts here.

label start:

    play music "fairytale.mp3"

    scene bg forest

    n "Once upon a time, there were three little pigs..."

    show pig1 neutral

    pig1 "I'm going to build my house out of straw!"

    show pig1 mad

    pig1 "But I bet that wolf will try to knock it down."

    show pig1 think

    pig1 "Maybe I should try building out of brick, like my friend suggested..."

    menu:

        "Nah, I'll stick with straw.":

            show pig1 neutral

            pig1 "Good old straw! It's cheap and light and easy to clean."

            jump wolf

        "Better safe than sorry. Brick it is!":

            show pig1 mad

            pig1 "Oof! I hope this is worth all the extra work."

            jump wolf

label wolf:

    play music "chase.mp3" fadeout 1.0

    show pig1 scared at left with move

    pig1 "Oh no! Here comes the wolf!"

    show wolf neutral at right with moveinright

    wolf "Little pig, little pig, let me in."

    show pig1 mad

    pig1 "Not by the hair of my chinny chin chin."

    show wolf think

    wolf "Then I'll huff..."
    wolf "...and I'll puff..."

    show wolf mad

    show pig1 scared

    wolf "...and I'll blow your house in."

    jump theend

label theend:

    stop music fadeout 2.0

    n "The End"

    return
