#задание 1 - это мой кривой вариант
import turtle
import time

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
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.shapesize(3)
red_light.color("grey")
red_light.penup()
red_light.setposition(0, 80)

yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.shapesize(3)
yellow_light.color("grey")
yellow_light.penup()
yellow_light.setposition(0, 0)

green_light = turtle.Turtle()
green_light.shape("circle")
green_light.shapesize(3)
green_light.color("grey")
green_light.penup()
green_light.setposition(0, -80)

class TrafficLight:

    def running (self):
        while True:
            red_light.color("red")
            time.sleep(7)
            red_light.color("grey")
            yellow_light.color("yellow")
            time.sleep(2)
            yellow_light.color("grey")
            green_light.color("green")
            time.sleep(7)
            green_light.color("grey")
            yellow_light.color("yellow")
            time.sleep(2)
            yellow_light.color("grey")

tf = TrafficLight()
tf.running()

turtle.mainloop()

