#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(joe, sides):
    for s in range (sides):
        joe.forward(50)
        joe.right(360/sides)
 
def fillCorner(john, corner):
     #draw a big square
     drawSquare(john, 100)
     
     if corner == 1:
         john.begin_fill()
         drawSquare(john, 50)
         john.end_fill()
     elif corner == 2:
         john.forward(50)
         john.begin_fill()
         drawSquare(john, 50)
         john.end_fill()
     elif corner == 3:
         john.penup()
         john.goto(0,-50)
         john.pendown()
         john.begin_fill()
         drawSquare(john, 50)
         john.end_fill()
         

def squaresInSquares(myTurtle, num_squares):
    
    for i in range(num_squares):
        size = (i + 1) * 20
        myTurtle.penup()
        myTurtle.goto(-size / 2, size / 2)
        myTurtle.pendown()
        drawSquare(myTurtle, size)

         
     
def main():
    myTurtle = turtle.Turtle()
    #Run each code by removing (#)
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 9) #draw a nonagon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    


main()
