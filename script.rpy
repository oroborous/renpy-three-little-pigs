define n = Character("Narrator")
define pig1 = Character("First Little Piggy", color="#FFD5EA")
define pig2 = Character("Second Little Piggy", color="#928168")
define pig3 = Character("Third Little Piggy", color="#D5B683")
define w = Character("Big Bad Wolf", color="#728194")

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

    show pig1 scared at right with move

    pig1 "Oh no! Here comes the wolf!"

    show wolf neutral at left with moveinleft

    w "Little pig, little pig, let me in."

    show pig1 mad

    pig1 "Not by the hair of my chinny chin chin."

    show wolf think

    w "Then I'll huff..."
    w "...and I'll puff..."

    show wolf mad

    show pig1 scared

    stop music fadeout 1.0

    w "...and I'll blow your house in."

    show wolf puff

    play sound "blow.mp3"

    w "Phhhhhhwwwwwwww.......!"

    queue sound "straw house crash.mp3"

    jump theend

label theend:
    hide wolf with moveoutleft

    show pig1 sad at center with move

    pig1 "Oh dear..."

    play music "fairytale.mp3"

    show pig2 sad at right with moveinright

    pig2 "This is terrible!"

    show pig3 sad at left with moveinleft

    pig3 "Whatever shall we do?"

    stop music fadeout 2.0

    n "To be continued..."

    return
