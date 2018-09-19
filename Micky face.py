import turtle

bg = turtle.Screen()
bg.bgcolor("silver")

fred = turtle.Turtle()
fred.shape ("turtle")
fred.speed(10)

def draw_circle(turtle, color, size, x,y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  
draw_circle(fred, "red", 80, 0, -60)
draw_circle(fred, "red", 45, 60, 60)
draw_circle(fred, "red", 45, -60, 60)
