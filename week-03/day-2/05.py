from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def draw(x,y):
    teal_line = canvas.create_line(x, y, x+50, y+50 )
draw(5, 5)
draw(150, 0)
draw(100, 0)

root.mainloop()