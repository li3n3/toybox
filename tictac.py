SPACE_DICT = {"a1": " ", "b1": " ", "c1": " ",
              "a2": " ", "b2": " ", "c2": " ",
              "a3": " ", "b3": " ", "c3": " "}

def showboard():
    # prints out a sweet board where each box is named with a number/letter
    board = ("  A   B   C\n"
             "1 {a1} | {b1} | {c1}\n"
             "  - * - * -\n"
             "2 {a2} | {b2} | {c2}\n"
             "  - * - * -\n"
             "3 {a3} | {b3} | {c3}\n").format(**SPACE_DICT)
    print board

def tictactime():
    '''Start with a blank board, play turns, and announce the winner'''
    showboard()
    winner = playturn('X')
    if winner == 'X' or winner == 'O':
        print "Nice playing! Looks like the winner was {0}.".format(winner)
    else:
        print "Bummer. Looks like the winner was {0}".format(winner)

def winning():
    winning_conditions = [SPACE_DICT["a1"] == SPACE_DICT["b1"] == SPACE_DICT["c1"]
                          and SPACE_DICT["a1"] != " ",
                          SPACE_DICT["a2"] == SPACE_DICT["b2"] == SPACE_DICT["c2"]
                          and SPACE_DICT["a2"] != " ",
                          SPACE_DICT["a3"] == SPACE_DICT["b3"] == SPACE_DICT["c3"]
                          and SPACE_DICT["a3"] != " ",
                          SPACE_DICT["a1"] == SPACE_DICT["a2"] == SPACE_DICT["a3"]
                          and SPACE_DICT["a1"] != " ",
                          SPACE_DICT["b1"] == SPACE_DICT["b2"] == SPACE_DICT["b3"]
                          and SPACE_DICT["b1"] != " ",
                          SPACE_DICT["c1"] == SPACE_DICT["c2"] == SPACE_DICT["c3"]
                          and SPACE_DICT["c1"] != " ",
                          SPACE_DICT["a1"] == SPACE_DICT["b2"] == SPACE_DICT["c3"]
                          and SPACE_DICT["a1"] != " ",
                          SPACE_DICT["c1"] == SPACE_DICT["b2"] == SPACE_DICT["a3"]
                          and SPACE_DICT["c1"] != " "]
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
    if turn not in SPACE_DICT:
        print "Hmm, that's not a board space. Try something like a2 or c3."
        print
        return playturn(player)
    # or it's a good input, but the space is already played, and we ask for
    # something else
    elif SPACE_DICT[turn] == 'X' or SPACE_DICT[turn] == 'O':
        print "That spot's already played. Try another!"
        print
        return playturn(player)
    # or it's a legit good input, and we assign that value in SPACE_DICT
    else:
        SPACE_DICT[turn] = player
        # and we print that on the board
        showboard()
        # and we don't keep playing if winning happened
        if winning():
            return player
        # or if there was a tie and the board is full
        elif ' ' not in SPACE_DICT.values():
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
    print "Oh good; me too. X goes first. Let's begin!"
    tictactime()
else:
    print "Hmm. That didn't look like either y or n."
