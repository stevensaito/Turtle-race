#!/bin/python3
#winner is the turtle that has moved the furthest in a 100 moves

from turtle import * #for shape
from random import randint #for random library

speed(0) #speeds up drawing 0 is faster than 10
penup()
goto(-140, 140)

for step in range(16): #range(some number) is how you set how many lines are drawn
  write(step, align='center') #align the lines center
  right(90) #turn 90 degress
  forward(10) #move forward (right) 10 spaces
  for dash in range (10): #for 10 dashes,   this is extra, remove and
      #unindent to return to original
      pendown() #puts pen down to draw line
      forward(10)
      penup() #pick up pen to stop drawing line
      forward(10)
  backward(210)
  left(90)
  forward(20)
  #end of loop
  
#steve Turtle
steve = Turtle() #creates the turtle named ada
steve.color('red') #sets the color of the turtle
steve.shape('turtle') #sets the shape of ada
#set ada at the start
steve.penup()
steve.goto(-160, 100)
steve.pendown()

  
#raizha Turtle
raizha = Turtle() #creates the turtle named ada
raizha.color('blue') #sets the color of the turtle
raizha.shape('turtle') #sets the shape of ada
#set ada at the start
raizha.penup()
raizha.goto(-160, 70)
raizha.pendown()

for turn in range (100):
    steve.forward(randint(1,5))
    raizha.forward(randint(1,5))