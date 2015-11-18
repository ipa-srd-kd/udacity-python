import turtle

def draw_square():
  for i in range(0,4):
    brad.forward(100)
    brad.right(90)
      
def draw_circle():
  angie.circle(100)

def draw_triangle():
  for i in range(0,3):
    lucy.right(120)
    lucy.forward(100)
  

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("blue","red")
brad.speed(100)

angie = turtle.Turtle()
angie.shape("arrow")
angie.color("blue")
angie.speed(100)
  
lucy = turtle.Turtle()
lucy.shape("circle")
lucy.color("green")

#for i in range(0,50):
  #draw_square()
  #brad.right(10) 
  
for i in range(0,500):
  draw_circle()
  angie.right(2)
  angie.forward(2)
#draw_triangle()

window.exitonclick()

