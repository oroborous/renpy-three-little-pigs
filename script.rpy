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

        "But straw houses are so beautiful.":

            show pig1 neutral

            pig1 "Good old straw! It's cheap and light and easy to clean."

            jump wolf

        "Hah! Wolves don't scare me!":

            show pig1 mad

            pig1 "I'm not scared of the big bad wolf! Straw will be just fine."

            jump wolf

label wolf:

    play music "chase.mp3" fadeout 1.0

    play sound "wolf howl.mp3"

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

    #play sound "blow.mp3"

    #play sound "straw house crash.mp3"

    jump theend

label theend:

    stop music fadeout 2.0

    n "The End"

    return
