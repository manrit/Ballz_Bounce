#Manrit 
#May 26 2022
#Balls Bounce

import turtle
import random

window = turtle.Screen()
window.delay(0)
window.tracer(2)
window.screensize(500,500)
window.setworldcoordinates(-300,-250,300,250)
window.title('Balls Bounce')

def createTurtle():
    #creating a ball
    t=turtle.Turtle()
    t.shape('circle')
    t.color('red')
    t.up()
    #assigning a random direction 
    t.setheading(random.randint(0,360))
    return t

#did ball hit the edge?
def turtle_bounce(t):
    x,y=t.pos()
    width,height=t.getscreen().screensize()
    #checking coordinates
    if x<-width/2 or x>width/2 or y<-height/2 or y>height/2:
        return True 
    return False 

ballz=[]
for i in range(5):
    ballz.append(createTurtle())

while True:

    for b in ballz:
        b.forward(5)
        x,y=b.pos()
        #did it hit the edges??
        if turtle_bounce(b):
            b.forward(-5)
            #ball.backward(5)
            b.setheading(random.randint(0,360))
