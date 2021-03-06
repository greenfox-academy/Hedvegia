from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

for i in range(16):
    line = canvas.create_line(0+i*20, 0, 300-i*20, 300, fill='yellow')
    line = canvas.create_line(0, 0+i*20, 300, 300-i*20, fill='yellow')

root.mainloop()