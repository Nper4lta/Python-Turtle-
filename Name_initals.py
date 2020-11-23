
import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t2.ht()
t2.penup()
t2.begin_fill()
t2.color("black","#000000")
l = 25
w = 100

#First Letter
t.begin_fill()
t.color("black","#000000")

#First Rectangle
for _ in range(4):
   
  # drawing length
  if _% 2 == 0:
    t.forward(l) # Forward turtle by l units
    t.right(90) # Turn turtle by 90 degree
 
  # drawing width
  else:
    t.forward(w) # Forward turtle by w units
    t.right(90) # Turn turtle by 90 degree
    
#The Diagonal
t.penup()
t.forward(l)
t.pendown()
t.left(10)

for _ in range(4):
   
  # drawing length
  if _% 2 == 0:
    t.forward(25) # Forward turtle by l units
    t.right(90) # Turn turtle by 90 degree
 
  # drawing width
  else:
    t.forward(w) # Forward turtle by w units
    t.right(90) # Turn turtle by 90 degree

#Second Rectangle
t.penup()
t.forward(l+17)
t.pendown()
t.right(10)

for _ in range(4):
   
  # drawing length
  if _% 2 == 0:
    t.forward(l) # Forward turtle by l units
    t.right(90) # Turn turtle by 90 degree
  # drawing width
  else:
    t.forward(w) # Forward turtle by w units
    t.right(90) # Turn turtle by 90 degree
t.end_fill()
t.ht()

#Lastname

t2.setx(100)
t2.sety(8)
#t2.goto(100,8)
t2.pendown()
t2.st()
#Rectangle for P
for _ in range(4):
   
  # drawing length
  if _% 2 == 0:
    t2.forward(l) # Forward turtle by l units
    t2.right(90) # Turn turtle by 90 degree
 
  # drawing width
  else:
    t2.forward(w) # Forward turtle by w units
    t2.right(90) # Turn turtle by 90 degree

#Half Circle for P
t2.penup()
t2.forward(l)
t2.pendown()

t2.left(10)
t2.circle(-30,200)

t2.penup()
t2.goto(125,-36.09)
t2.left(10)
t2.pendown()
t2.circle(-15,-174)
t2.end_fill()
t2.ht()
