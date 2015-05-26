def showboard():
    # prints out a sweet board where each box is named with a number/letter
    print "  A   B   C"
    print "1 {a1} | {b1} | {c1}".format(**space_dict)
    print "  - * - * -"
    print "2 {a2} | {b2} | {c2}".format(**space_dict)
    print "  - * - * -"
    print "3 {a3} | {b3} | {c3}".format(**space_dict)

space_dict = {"a1": " ", "b1": " ", "c1": " ",
              "a2": " ", "b2": " ", "c2": " ",
              "a3": " ", "b3": " ", "c3": " "}

def tictactime():
# we start with a blank board
    showboard()
    # we'll get the winner back from playturn:
    winner = playturn('X')
    if winner == 'X' or winner == 'O':
        print "Nice playing! Looks like the winner was " + str(winner) + "."
    else:
        print "Bummer. Looks like the winner was " + str(winner)

def winning():
    winning_conditions = [space_dict["a1"] == space_dict["b1"] == space_dict["c1"]
                          and space_dict["a1"] != " ",
                          space_dict["a2"] == space_dict["b2"] == space_dict["c2"]
                          and space_dict["a2"] != " ",
                          space_dict["a3"] == space_dict["b3"] == space_dict["c3"]
                          and space_dict["a3"] != " ",
                          space_dict["a1"] == space_dict["a2"] == space_dict["a3"]
                          and space_dict["a1"] != " ",
                          space_dict["b1"] == space_dict["b2"] == space_dict["b3"]
                          and space_dict["b1"] != " ",
                          space_dict["c1"] == space_dict["c2"] == space_dict["c3"]
                          and space_dict["c1"] != " ",
                          space_dict["a1"] == space_dict["b2"] == space_dict["c3"]
                          and space_dict["a1"] != " ",
                          space_dict["c1"] == space_dict["b2"] == space_dict["a3"]
                          and space_dict["c1"] != " "]
    if True in winning_conditions:
        return True
    else:
        return False


def playturn(player):
    turn = raw_input("What space would you like to play, {0}?\n".format(player))
    # just in case it's caps
    turn = turn.lower()
    # We expect something like a2, b1, c3
    # either it's a bad input (not a board position)
    # and we ask for something else
    if turn not in space_dict:
        print "Hmm, that's not a board space. Try something like a2 or c3."
        print
        return playturn(player)
    # or it's a good input, but the space is already played, and we ask for
    # something else
    elif space_dict[turn] == 'X' or space_dict[turn] == 'O':
        print "That spot's already played. Try another!"
        print
        return playturn(player)
    # or it's a legit good input, and we assign that value in space_dict
    else:
        space_dict[turn] = player
        # and we print that on the board
        showboard()
        # and we don't keep playing if winning happened
        if winning():
            return player
        # or if there was a tie and the board is full
        elif ' ' not in space_dict.values():
            # print "Aw, that's a tie. Nice playing!"
            return "no one.  :("
        else:
            if player == 'X':
                return playturn('O')
            else:
                return playturn('X')


# Let's start this party!
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
    tictactime()
else:
    print "Hmm. That didn't look like either y or n."
