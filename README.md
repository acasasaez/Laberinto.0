# Laberinto.0
En esta tarea se nos ha pedido que elaborásemos un programa que generase un laberinto.

Como siempre, para poder presentar nuestro trabajo inicialmente hemos tenido que crear un repositorio donde subir el mismo, aquí le dejo el enlacen del mío: https://github.com/acasasaez/Laberinto.0.git

Por otro lado, tle adjunto la imagen del diagrama de flujo que representa mi programa:
![NNNN - copia](https://user-images.githubusercontent.com/91721826/145292962-45e079b5-c871-4b77-85a5-e539ee17cf0b.jpg)
Por último, aquí le dejo el código de mi juego:
```from math import inf
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
