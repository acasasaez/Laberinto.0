from math import inf
import turtle
ventana = turtle.Screen()
ventana.bgcolor ("purple")
ventana.title ("Laberinto")
ventana.setup(500,500)
class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("pink")
        self.penup()
        self.speed(0)

laberinto = []
laberinto_1 = [" XXXX",
               " X   ",
               " X X ",
               "   X ",
               "XXXX "]
laberinto.append(laberinto_1)
def iniciar_lab(laberinto):
    for file in range (len(laberinto)):
        for column in range(len(laberinto[file])):
            letra_X = laberinto [file][column]
            screen_x = -288 + (column * 4)
            screen_y = 288 - (file * 4)
            if letra_X == "X":
                pen.goto (screen_x, screen_y)
                pen.stamp()
pen = Pen()
iniciar_lab(laberinto[0])