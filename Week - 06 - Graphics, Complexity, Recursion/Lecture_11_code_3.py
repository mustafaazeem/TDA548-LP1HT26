'''
We learn how to use Coordinate system provided by graphics library 
'''
from graphics import *

win = GraphWin('Coordinate test system', 600, 600)

# first pair 0,0 represents bottom-left, and second pair 100,100 represents top-right 
win.setCoords(0, 0, 100, 100 )

bomb = Circle(Point(2,2), 1)
bomb.setFill('red')
bomb.draw(win)

for i in range(30):
    bomb.move(1, 1)
    time.sleep(0.2)
win.getKey()