import turtle
ventana = turtle.Screen()
ventana.bgcolor ("purple")
ventana.title ("Laberinto")
ventana.setup(5,5)
class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("pink")
        self.penup()
        self.speed(0)