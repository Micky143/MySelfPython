'''
# A Flower program:
from turtle import *
color('red', 'green')
begin_fill()
while True:
    forward(500)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
#-----------------------------------------------------------------------------------------------------------------------------------
# A square spiral program :-
'''
from turtle import *
for i in range(500): # this "for" loop will repeat these functions 500 times
    forward(i)
    left(91)
'''
#-----------------------------------------------------------------------------------------------------------------------------------
#A colorful hexagon spiral program:
'''
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
'''


#-----------------------------------------------------------------------------------------------------------------------------------
#A blue flowers program:
'''
from turtle import *
import random

for n in range(60):
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    for i in range(6):
        circle(circle_size)
        left(60)
'''

#-----------------------------------------------------------------------------------------------------------------------------------
# Stamping

from turtle import *

penup()

for i in range(30, -1, -1):
    stamp()
    left(i)
    forward(20)





































































































































