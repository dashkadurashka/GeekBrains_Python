#задание 1 с помощью преподавателя

import turtle
import time


class TrafficLight:
    __color = [(80, 0, -80), ("red", "yellow", "green"), (7, 2, 7), "grey"]

    def __init__(self):
        self.frame()

    def frame(self):
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.color("black")
        pen.width(3)
        pen.hideturtle()

        pen.penup()
        pen.setposition(-60, 120)
        pen.pendown()
        pen.forward(120)
        pen.right(90)
        pen.forward(240)
        pen.right(90)
        pen.forward(120)
        pen.right(90)
        pen.forward(240)

    def lights(self):
        self.light = turtle.Turtle()
        self.light.shape("circle")
        self.light.shapesize(3)
        self.light.color("grey")
        self.light.penup()

    def running(self):
        i = 0
        while True:
            self.lights()
            self.light.setposition(0, self.__color[0][i])
            self.light.color(self.__color[1][i])
            time.sleep(self.__color[2][i])
            self.light.color(self.__color[3])
            i += 1
            if i == 3:
                i = 0


tf = TrafficLight()
tf.running()

turtle.mainloop()
