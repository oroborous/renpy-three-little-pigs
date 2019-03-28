# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define pig1 = Character("Pig 1")
define pig2 = Character("Pig 2")
define pig3 = Character("Pig 3")
define wolf = Character("Big Bad Wolf")

# The game starts here.

label start:

    scene bg forest
    
    n "Once upon a time, there were three little pigs..."

    show pig1 neutral

    pig1 "I'm going to build my house out of straw!"
    
    show pig1 mad
    
    pig1 "But I bet that wolf will try to knock it down."
    
    show pig1 sad
    
    menu:

        pig1 "Maybe I should try building out of brick, like my friend Pig 3 suggested..."

        "Nah, I'll stick with straw.":
        
            pig1 "Good old straw! It's cheap and light and easy to clean."

            jump straw

        "Better safe than sorry. Brick it is!":
        
            pig1 "Oof! I hope this is worth all the extra work."

            jump brick
            
label straw:

    show pig1 scared
    
    pig1 "Oh no! Here comes the wolf!"
    
    wolf "Little pig, little pig, let me in."
    
    pig1 "Not by the hair of my chinny chin chin."
    
    wolf "Then I'll huff, and I'll puff, and I'll blow your house in."
    
    jump theend
    
label brick:

    show pig1 scared
    
    pig1 "I think I hear the wolf outside."
    
    
label theend:    
    
    n "The End"

    # This ends the game.

    return
