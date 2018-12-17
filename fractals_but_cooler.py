from tkinter import *
import turtle
import random
from PIL import ImageTk, Image


# turtle_speed = 5

# testing
def doSomething():
    print("did something")


# The triangle fractal
def triangleFractal():
    wn = turtle.Screen()
    wn.bgcolor("green")
    brush = turtle.Turtle()
    brush.ht()
    brush.speed(5)

    brush.pencolor('orange')

    points = [[-175, -125], [0, 175], [175, -125]]  # size of triangle

    def getMid(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)  # find midpoint

    def triangle(points, depth):
        brush.up()
        brush.goto(points[0][0], points[0][1])
        brush.down()
        brush.goto(points[1][0], points[1][1])
        brush.goto(points[2][0], points[2][1])
        brush.goto(points[0][0], points[0][1])

        if depth > 0:
            triangle([points[0],
                      getMid(points[0], points[1]),
                      getMid(points[0], points[2])],
                     depth - 1)
            triangle([points[1],
                      getMid(points[0], points[1]),
                      getMid(points[1], points[2])],
                     depth - 1)
            triangle([points[2],
                      getMid(points[2], points[1]),
                      getMid(points[0], points[2])],
                     depth - 1)

    triangle(points, 4)


def snowflakeFractal():
    # setup the window with a background color
    # wn = turtle.Screen()
    # wn.bgcolor("cyan")
    brush = turtle.Turtle()
    brush.ht()
    brush.speed(5)
    brush.pencolor('orange')

    # move the pen into starting position
    brush.penup()
    brush.forward(10)
    brush.left(45)
    brush.pendown()
    # brush.color(random.choice(sfcolor))

    # draw branch 8 times to make a snowflake
    for i in range(8):
        for i in range(3):
            for i in range(3):
                brush.forward(10.0 * 10 / 3)
                brush.backward(10.0 * 10 / 3)
                brush.right(45)
            brush.left(90)
            brush.backward(10.0 * 10 / 3)
            brush.left(45)
        brush.right(90)
        brush.forward(10.0 * 10)
        brush.left(45)


def snowStorm():
    # setup the window with a background color
    wn = turtle.Screen()
    wn.bgcolor("cyan")
    brush = turtle.Turtle()
    brush.ht()
    brush.speed(1000)
    brush.pencolor('orange')

    # create a function to create different size snowflakes
    def snowflake(size):

        # move the pen into starting position
        brush.penup()
        brush.forward(10 * size)
        brush.left(45)
        brush.pendown()
        # brush.color(random.choice(sfcolor))

        for i in range(8):
            branch(size)
            brush.left(45)

    def branch(size):
        for i in range(3):
            for i in range(3):
                brush.forward(10.0 * size / 3)
                brush.backward(10.0 * size / 3)
                brush.right(45)
            brush.left(90)
            brush.backward(10.0 * size / 3)
            brush.left(45)
        brush.right(90)
        brush.forward(10.0 * size)

    for i in range(50):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        sf_size = random.randint(1, 4)
        brush.penup()
        brush.goto(x, y)
        brush.pendown()
        snowflake(sf_size)


def squareFractal():
    wn = turtle.Screen()
    wn.bgcolor("yellow")

    def s(n, l):

        if n == 0:  # stop conditions

            # draw filled rectangle

            turtle.color('black')
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(l)
                turtle.left(90)
            turtle.end_fill()

        else:  # recursion

            # around center point create 8 smalles rectangles.
            # create two rectangles on every side
            # so you have to repeat it four times

            for _ in range(4):
                # first rectangle
                s(n - 1, l / 3)
                turtle.forward(l / 3)

                # second rectangle
                s(n - 1, l / 3)
                turtle.forward(l / 3)

                # go to next corner
                turtle.forward(l / 3)
                turtle.left(90)

            # update screen
            turtle.update()

    # stop updating screen (to make it faster)
    turtle.tracer(0)

    # start
    s(4, 400)

    # event loop
    turtle.done()


def treehelper(length, n):
    turtle.ht()
    turtle.pencolor('white')
    turtle.speed(300000000000000000000000000000000000000000000)
    wn = turtle.Screen()
    wn.bgcolor("black")

    if length < (length / n):
        return
    turtle.forward(length)
    turtle.left(45)
    treehelper(length * 0.5, length / n)
    turtle.left(20)
    treehelper(length * 0.5, length / n)
    turtle.right(75)
    treehelper(length * 0.5, length / n)
    turtle.right(20)
    treehelper(length * 0.5, length / n)
    turtle.left(30)
    turtle.backward(length)
    return


def tree():
    length = 200
    n = 4
    treehelper(length, n)


'''
def increaseSpeed():
    turtle_speed = turtle_speed + 5

def decreaseSpeed():
    turtle_speed = turtle_speed - 5

def colorWheel():

    #will default to orange
    #because orange is a cool color
    color = 'orange'

    if(lineColorMenu.label("Black")):
        color = 'black'
        return 'black'
    elif(lineColorMenu.index("White") == 2234):
        color = 'white'
        return color
    elif(lineColorMenu.index("Red") == 3):
        color = 'red'
        return color

    elif(lineColorMenu.index("Blue") == 4):
        color = 'blue'
        return color   
    elif(lineColorMenu.index("Yellow") == 5):
        color = 'yellow'
        return color
    elif(lineColorMenu.index("Green") == 6):
        color = 'green'
        return color
    elif(lineColorMenu.index("Orange") == 7):
        color = 'orange'
        return color
    elif(lineColorMenu.index("Purple") == 8):
        color = 'purple'
        return color
    elif(lineColorMenu.index("Cyan") == 9):
        color = 'cyan'
        return color
    elif(lineColorMenu.index("Brown") == 10):
        color = 'brown'
        return color
'''


def clear():
    turtle.clearscreen()
    turtle.ht()


def exit():
    turtle.bye()


#
# def tree(length, n):
#     if length < (length / n):
#         return
#     turtle.forward(length)
#     turtle.left(45)
#     tree(length * 0.5, length / n)
#     turtle.left(20)
#     tree(length * 0.5, length / n)
#     turtle.right(75)
#     tree(length * 0.5, length / n)
#     turtle.right(20)
#     tree(length * 0.5, length / n)
#     turtle.left(30)
#     turtle.backward(length)
#     return

root = Tk()
menu = Menu(root)
root.config(menu=menu)

fractalMenu = Menu(menu)
menu.add_cascade(label="Fractals", menu=fractalMenu)
fractalMenu.add_command(label="Square", command=squareFractal)
fractalMenu.add_command(label="Triangle", command=triangleFractal)
fractalMenu.add_command(label="Snowflake", command=snowflakeFractal)
fractalMenu.add_command(label="Snowstorm", command=snowStorm)
fractalMenu.add_command(label="Tree", command=tree)
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Increase Draw Speed", command=increaseSpeed)
# editMenu.add_command(label="Decrease Draw Speed", command=decreaseSpeed)
editMenu.add_command(label="Clear", command=clear)
editMenu.add_command(label="Exit", command=exit)

lineColorMenu = Menu(menu)
menu.add_cascade(label="Line Color", menu=lineColorMenu)
lineColorMenu.add_radiobutton(label="Black", value=1, command=doSomething)
lineColorMenu.add_radiobutton(label="White", command=doSomething)
lineColorMenu.add_radiobutton(label="Red", value=4, command=doSomething)
lineColorMenu.add_radiobutton(label="Blue", command=doSomething)
lineColorMenu.add_radiobutton(label="Yellow", command=doSomething)
lineColorMenu.add_radiobutton(label="Green", command=doSomething)
lineColorMenu.add_radiobutton(label="Orange", command=doSomething)
lineColorMenu.add_radiobutton(label="Purple", command=doSomething)
lineColorMenu.add_radiobutton(label="Cyan", command=doSomething)
lineColorMenu.add_radiobutton(label="Brown", command=doSomething)

'''
lineColorMenu.add_command(label="Red", command=doSomething)
lineColorMenu.add_command(label="Blue", command=doSomething)
lineColorMenu.add_command(label="Yellow", command=doSomething)
lineColorMenu.add_command(label="Green", command=doSomething)
lineColorMenu.add_command(label="Orange", command=doSomething)
lineColorMenu.add_command(label="Purple", command=doSomething)
lineColorMenu.add_command(label="Cyan", command=doSomething)
lineColorMenu.add_command(label-"Brown", command=doSomething)
'''

fillColorMenu = Menu(menu)
menu.add_cascade(label="Fill Color", menu=fillColorMenu)
fillColorMenu.add_command(label="Black", command=doSomething)
fillColorMenu.add_command(label="White", command=doSomething)
fillColorMenu.add_command(label="Red", command=doSomething)
fillColorMenu.add_command(label="Blue", command=doSomething)
fillColorMenu.add_command(label="Yellow", command=doSomething)
fillColorMenu.add_command(label="Green", command=doSomething)
fillColorMenu.add_command(label="Orange", command=doSomething)
fillColorMenu.add_command(label="Purple", command=doSomething)
fillColorMenu.add_command(label="Cyan", command=doSomething)
fillColorMenu.add_command(label="Brown", command=doSomething)

backgroundColorMenu = Menu(menu)
menu.add_cascade(label="Background", menu=backgroundColorMenu)
backgroundColorMenu.add_command(label="Black", command=doSomething)
backgroundColorMenu.add_command(label="White", command=doSomething)
backgroundColorMenu.add_command(label="Red", command=doSomething)
backgroundColorMenu.add_command(label="Blue", command=doSomething)
backgroundColorMenu.add_command(label="Yellow", command=doSomething)
backgroundColorMenu.add_command(label="Green", command=doSomething)
backgroundColorMenu.add_command(label="Orange", command=doSomething)
backgroundColorMenu.add_command(label="Purple", command=doSomething)
backgroundColorMenu.add_command(label="Cyan", command=doSomething)
backgroundColorMenu.add_command(label="Brown", command=doSomething)

'''
colorMenu.add_command(label="Line Color", command=doSomething)
colorMenu.add_command(label="Fill Color", command=doSomething)
colorMenu.add_command(label="Background Color", command=doSomething)
'''
img = ImageTk.PhotoImage(Image.open("project_image.jpg"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
