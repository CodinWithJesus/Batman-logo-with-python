import turtle
import math

kalu = turtle.Turtle()
kalu.speed(500)

window = turtle.Screen()
window.bgcolor("black")
kalu.color("white")

hehe = 60

kalu.left(200)
kalu.penup()
kalu.goto(-7 * hehe, 0)
kalu.pendown()

for a in range(-7 * hehe, -3 * hehe, 1):
    x = a / hehe
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalu.goto(a, y * hehe)

for a in range(-3 * hehe, -1 * hehe - 1, 1):
    x = a / hehe
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalu.goto(a, y * hehe)

kalu.goto(-1 * hehe, 3 * hehe)
kalu.goto(int(-0.5 * hehe), int(2.2 * hehe))
kalu.goto(int(0.5 * hehe), int(2.2 * hehe))
kalu.goto(1 * hehe, 3 * hehe)
print("I am batman")
for a in range(1 * hehe + 1, 3 * hehe + 1, 1):
    x = a / hehe
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalu.goto(a, y * hehe)

for a in range(3 * hehe + 1, 7 * hehe + 1, 1):
    x = a / hehe
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalu.goto(a, y * hehe)

for a in range(7 * hehe, 4 * hehe, -1):
    x = a / hehe
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalu.goto(a, y * hehe)

for a in range(4 * hehe, -4 * hehe, -1):
    x = a / hehe
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    kalu.goto(a, y * hehe)

for a in range(-4 * hehe - 1, -7 * hehe - 1, -1):
    x = a / hehe
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalu.goto(a, y * hehe)

kalu.penup()
kalu.goto(300, 300)
turtle.done()