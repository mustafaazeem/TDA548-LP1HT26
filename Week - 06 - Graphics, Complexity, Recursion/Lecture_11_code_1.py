'''
We learn how to use a simple graphics library in this code 
the library we use is graphics.py, which is a simplification 
on top of tkinter. It is provided by our course book
'''

from graphics import *      # not a good way to import everything from a library 

my_win = GraphWin("Graphics Testing", 600, 400)

# How to draw a point 
p1 = Point(100, 100)
p1.setFill('red')
p1.draw(my_win)     # do not forget to actually draw on your window


# Draw a line 
line_1 = Line(Point(10,390), Point(400, 390))
line_1.setFill('green')
line_1.draw(my_win)

# Draw a circle 
circle_center = Point(20, 20)
radius = 10

# use a circle to represent a bomb
bomb = Circle(circle_center, radius)
bomb.setFill('blue')
bomb.draw(my_win)

# move the circle (bomb) on window 
for i in range(100):
    bomb.move(i,1)
    time.sleep(0.1)


# keep the window on screen by let it wait for mouse click 
mouse_location = my_win.getMouse()
print(mouse_location)


