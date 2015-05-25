# test values to print
# a1 = "X"
# b1 = "X"
# c1 = "O"

# a2 = "O"
# b2 = "O"
# c2 = "X"

# a3 = "X"
# b3 = "O"
# c3 = "X"

def showboard():
    # prints out a sweet board where each box is named with a number/letter
    print "  A   B   C"
    print "1 {a1} | {b1} | {c1}".format(**space_dict)
    print "  - * - * -"
    print "2 {a2} | {b2} | {c2}".format(**space_dict)
    print "  - * - * -"
    print "3 {a3} | {b3} | {c3}".format(**space_dict)

# showboard()

print "Hey there! Welcome to tic-tac-toe. I'll be your robot host today."
print "Grab a friend, or play against yourself. (I'm working on my skills.)"
print "Each spot is named by a number and a letter, like this:"
print
print"  A   B   C"
print "1   |   |  "
print "  - * - * -"
print "2   |   |  "
print "  - * - * -"
print "3   |   |  "
print

print "When it's your turn to play, type the letter and number of the spot "\
      "you'd like to play, e.g. 'c2':"
print

print"  A   B   C"
print "1   |   |  "
print "  - * - * -"
print "2   |   | X"
print "  - * - * -"
print "3   |   |  "
print

ready = raw_input("The game ends when someone gets three in a row, or no more moves are "\
      "possible. Ready? Type y or n.\n")
if ready == "n":
    print "No problem. Grab me a byte to eat and come back later?"
elif ready == "y":
    print "Oh good; me too."
else:
    print "Hmm. That didn't look like either y or n."

# Our starting board:
# a1, b1, c1 = " ", " ", " "
# a2, b2, c2 = " ", " ", " "
# a3, b3, c3 = " ", " ", " "

space_dict = {"a1": " ", "b1": " ", "c1": " ",
              "a2": " ", "b2": " ", "c2": " ",
              "a3": " ", "b3": " ", "c3": " "}

# spaces = ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"]
# played_spaces = ['a2', 'b2']
    
# winning_conditions = [a1 == b1 == c1 and a1 != ' ', a2 == b2 == c2 and a2 != ' ',
#                       a3 == b3 == c3 and a3 != ' ', a1 == a2 == a3 and a1 != ' ',
#                       b1 == b2 == b3 and b1 != ' ', c1 == c2 == c3 and c1 != ' ',
#                       a1 == b2 == c3 and a1 != ' ', c1 == b2 == a3 and c1 != ' ']

winning_conditions = [space_dict["a1"] == space_dict["b1"] == space_dict["c1"]
                      and space_dict["a1"] != " "]

# the_game
def tictactime():
# we start with a blank board
    showboard()

    if True in winning_conditions:
        print "Someone won!"
        print "And that someone was ... the winner!"
    if length(played_spots) == 9:
        return "Aw, that's a tie. Nice playing!"


def playturn(player):
# X plays a turn
    turn = raw_input("What space would you like to play, {0}?\n".format(player))
    # just in case it's caps
    turn = turn.lower()
    # We expect something like a2, b1, c3
    # either it's a bad input (not a board position, or already taken)
    # and we ask for something else
    if turn not in spaces:
        print "Hmm, that's not a board space. Try something like a2 or c3."
        print
        playturn(player)
    # or it's a good input, but the space is already played
    elif turn in played_spaces:
        print "That spot's already played. Try another!"
        print
        playturn(player)
    # or it's a legit good input, and we add it to the played spaces
    else:
        played_spaces.append(turn)
        # and we print that on the board
        print "turn is " + turn
        turn = player
        print "turn is " + turn

playturn("X")




# then O plays a turn
#     same stuff as above

# this continues until one of the 8 winning conditions is met
# OR until all positions are filled

# then it tells us who won 
# or that no one won 
# and then we're done (maybe it asks us to play again?)

