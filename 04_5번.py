from graphics import *; 

def main():
    win = GraphWin("Dice",200,200)
    line1 = Line(Point(10, 0), Point(30,0))
    line2 = Line(Point(10, 0), Point(0,10))
    line3 = Line(Point(30 ,0), Point(20,10))
    line4 = Line(Point(0, 10), Point(20,10))
    line5 = Line(Point(0, 10), Point(0,30))
    line6 = Line(Point(20,10),Point(20,30))
    line7 = Line(Point(0, 30), Point(20,30))
    line8 = Line(Point(20,30),Point(30,20))
    line9 = Line(Point(30,0), Point(30,20))


    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)
    line9.draw(win)

    win.getMouse()
    win.close()

main()