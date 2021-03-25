import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    
    (t, wn, map_bg_img) = irma_setup()
    
    
    with open('data/irma.csv','r',) as oFile:
        lines=[]
        for line in oFile.readlines():
            lines = lines + [line.strip().split(',')]
        lines = lines[1:]
        for entry in lines:
            entry[2] = float(entry[2])
            entry[3] = float(entry[3])
            entry[4] = float(entry[4])
        t.up()
        t.setx(lines[0][3])
        t.sety(lines[0][2])
        t.down()
        latx = 0
        lony = 0
        
        for entry in lines[1:]:
            latx = latx + 1
            lony = lony + 1
            t.goto(lines[latx][3],lines[lony][2])
            if entry[4]<=(74):
                t.color('white')
                t.pensize(0)
            elif entry[4]>=(74) and entry[4]<=(95):
                t.color('blue')
                t.write('1')
                t.pensize(2)
            elif entry[4]>=(96) and entry[4]<=(110):
                t.color('green')
                t.write('2')
                t.pensize(4)
            elif entry[4]>=(111) and entry[4]<=(129):
                t.color('yellow')
                t.write('3')
                t.pensize(6)
            elif entry[4]>=(130) and entry[4]<=(156):
                t.color('orange')
                t.write('4')
                t.pensize(8)
            elif entry[4]>=(157):
                t.color('red')
                t.write('5')
                t.pensize(10)
    wn.exitonclick()


if __name__ == "__main__":
    irma()


