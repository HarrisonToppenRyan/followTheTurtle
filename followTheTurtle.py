# Author :  Harrison Toppen-Ryan
# Description :  Follow the Turtle (HW 4), CSCI 141
# Date :  November 11th, 2020

# turtle 
import turtle
turtle.bgcolor("lightgreen") #background color 
a = turtle.Turtle() #paddle a
a.speed(0) #speed of paddle a
a.shape("turtle")#shape of paddle a
a.color("#FF0000")#red color 

b = turtle.Turtle() #paddle b
b.speed(0) #speed of paddle b
b.shape("turtle") #shape of paddle b
b.color("#008000") #green color 

c = turtle.Turtle() #paddle c
c.speed(0) #speed of paddle c
c.shape("turtle") #speed of paddle b
c.color("#0000FF") #blue color


for i in range(85): #all paddles move 85 steps, repeats one step until 85 steps are taken
    a.forward(i+5)# lines 25-27 paddle a speed and direction, with line and creates shape of turtle
    a.right(15)
    a.stamp()
    b.forward(i+5) # lines 28-32 paddle b speed and direction, removes line and creates shape of turtle
    b.right(14.5)
    b.up()
    b.stamp()
    b._delay(5)
    c.forward(i+5) # lines 33-37 paddle c speed and direction, removes line and creates shape of turtle
    c.right(14.2)
    c.up()
    c.stamp()
    c._delay(15)
   
   

# finish and display (calling the turtles)
turtle.done()

