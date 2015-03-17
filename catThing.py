
# Author: Jake Stocker
# Date: 06/27/2014
# Cat Thing?
# --------------------------------------
from swampy.TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

def square(turtle, length):
    for loop in range(4):
        fd(turtle, length)
        rt(turtle)


def inverse_arc(turtle,radius,angle):
    arcLength = 2 * math.pi * radius * angle / 360
    sides = int(arcLength / 3) + 1
    stepLength = arcLength / sides
    stepAngle = float(angle) / sides

    for loop in range(sides):
        fd(turtle, stepLength)
        rt(turtle, stepAngle)

def polyline(turtle, sides, length, angle):
    """ Draws number of angles with the given length
    and angle (in degrees) between them."""
    for loop in range(sides):
        fd(turtle, length)
        lt(turtle, angle)

def polygon(turtle, sides, length):
    angle = 360.0 / sides
    polyline(turtle, sides, length, angle)

def arc(turtle, radius, angle):
    arcLength = 2 * math.pi * radius * angle / 360
    sides = int(arcLength / 3) + 1
    stepLength = arcLength / sides
    stepAngle = float(angle) / sides
    polyline(turtle, sides, stepLength, stepAngle)

def circle(turtle, radius):
    arc(turtle, radius, 360)

def horn(turtle,size):
   rt(turtle,100)
   fd(turtle,size)
   lt(turtle,160)
   fd(turtle,size+5)
   rt(turtle,40)

def teeth(size):
    

   for loop in range(3):
       rt(bob,120)
       fd(bob,size)
       lt(bob,120)
       fd(bob,size)


   rt(bob,10)
   fd(bob,size)
   rt(bob,180)
   lt(bob,size)

   
   for loop in range(3):
       rt(bob,120)
       fd(bob,size)
       lt(bob,120)
       fd(bob,size)

   lt(bob,10)
   fd(bob,size)

def main():
   circle(bob,50)
   arc(bob,50,90)
   arc(bob,50,70)
   horn(bob,30)
   arc(bob,50,30)
   horn(bob,30)
   
   pu(bob)

   fd(bob,30)

   lt(bob,130)
  

   fd(bob,25)
   pd(bob)
   circle(bob,5)
   pu(bob)
   fd(bob,40)
   pd(bob)
   circle(bob,5)
   pu(bob)
   rt(bob)
   fd(bob,20)

   rt(bob,20)
   fd(bob,4)
   pd(bob)


   teeth(10)
       
  
   pu(bob)
   rt(bob)
   fd(bob,50)
   
   

   
    
               
main()

wait_for_user()

