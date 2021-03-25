import turtle
ja = turtle.Turtle()
ja.shape('turtle')
clock_angle = (30)

for i in range(12):
    ja.color("red")
    ja.up()
    ja.down()
    ja.fd(50)
    ja.color("blue")
    ja.fd(25)
    ja.up()
    ja.fd(15)
    ja.color("green")
    ja.stamp()
    ja.home()
    ja.right(clock_angle)
    clock_angle = clock_angle + 30

