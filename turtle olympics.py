import turtle
ja = turtle.Turtle()
Pi = 3.14159
radius = (100)
radius = int(radius)
circumference = 2 * Pi * radius

ja.color("yellow")
for i in range(30):
    ja.right(360//30)
    ja.fd(circumference//30) 

ja.left(180)
ja.right(45)
ja.up()
ja.fd(80)
ja.down()
ja.color("blue")
for i in range(30):
    ja.right(360//30)
    ja.backward(circumference//30)  

ja.left(180)
ja.right(45)
ja.up()
ja.fd(140)
ja.left(90)
ja.fd(150)
ja.down()
ja.color("black")
for i in range(30):
    ja.right(360//30)
    ja.backward(circumference//30)


ja.color("green")
ja.up()
ja.fd(30)
ja.left(90)
ja.down()
for i in range(30):
    ja.right(360//30)
    ja.fd(circumference//30) 


ja.color("red")
ja.up()
ja.right(90)
ja.fd(200)
ja.down()
for i in range(30):
    ja.right(360//30)
    ja.backward(circumference//30)  
