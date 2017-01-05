import turtle


def drawing(firstLevelMoves = None, secondLevelMoves = None, colors=None):
    while firstLevelMoves is None:
        firstLevelMoves = int(input("How many first level moves would you like to make: \n"))

    if secondLevelMoves is None:
        answer = str.lower(input("Would you like to also make second level moves?: y/n\n"))
        if answer == 'y':
            secondLevelMoves = int(input("How many second level moves would you like to make: \n"))

    if colors is None:
        answer = str.lower(input("Would you like to change color for each round/move?: y/n\n"))
        if answer == 'y':
            user_answr = str(input("What colors would you like to have (e.g. red, blue, green, purple, black: \n"))
            colors = user_answr.split(' ')

    turtle.hideturtle()
    turtle.setup(width=.9, height=0.90, startx=None, starty=None)
    turtle.penup()
    turtle.sety(350)
    turtle.pendown()

    for first in range(firstLevelMoves):
        for col in colors:
            turtle.color(col)
            turtle.forward(100)
            turtle.right(360 / firstLevelMoves)
            if secondLevelMoves is not None:
                for second in range(secondLevelMoves):
                    turtle.forward(50)
                    turtle.right(360 / secondLevelMoves)
    turtle.exitonclick()
    return

if __name__ == '__main__':
    drawing()
