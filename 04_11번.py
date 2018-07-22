from graphics import *

def main():
    win = GraphWin("Design a House",500,500)
    win.setCoords(0, 0, 200, 200)
    message = Text(Point(100,5),"")
    message.draw(win)

    # Draw the frame of the house
    message.setText("Click on lower left corner of the frame")
    frameLL = win.getMouse()
    frameLL.draw(win)
    message.setText("Click upper right corner of the frame")
    frameUR = win.getMouse()
    frameLL.undraw()
    Rectangle(frameLL, frameUR).draw(win)

    # Draw a door
    houseWidth = frameUR.getX() - frameLL.getX()
    doorWidth = 0.2 * houseWidth
    halfDoor = doorWidth/2.0
    message.setText("Click on the center of the top of the door")
    doorPt2 = win.getMouse()
    doorPt2.move(halfDoor, 0)
    doorX1 = doorPt2.getX() - doorWidth
    doorY1 = frameLL.getY()
    door = Rectangle(Point(doorX1,doorY1), doorPt2)
    door.setFill("red")
    door.draw(win)

    # Draw a window
    message.setText( "Click on the center of the window")
    windowCenter = win.getMouse()
    w1 = windowCenter.clone()
    winOff = 0.5 * halfDoor
    w1.move(-winOff,winOff)
    w2 = windowCenter.clone()
    w2.move(winOff, -winOff)
    Rectangle(w1,w2).draw(win)

    # Draw the roof
    message.setText( "Click on the peak of the roof")
    peak = win.getMouse()
    frameUL = frameUR.clone()
    frameUL.move(-houseWidth,0)
    roof = Polygon(frameUL, peak, frameUR)
    roof.draw(win)
    roof.setFill("black")
    
    message.setText( "Click anywhere to quit." )
    win.getMouse()
    win.close()

main()
