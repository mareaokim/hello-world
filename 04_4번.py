from graphics import *

def main():
    win=GraphWin("Winter Scene",500,500)
    win.setCoords(0,0,200,200)
    win.setBackground("blue")


    c1 = Circle(Point(50,40),40)
    c1.draw(win)
    c1.setFill("white")
    c1.setOutline("white")

    c2 = Circle(Point(50,100),30)
    c2.draw(win)
    c2.setFill("white")
    c2.setOutline("white")

    c3 = Circle(Point(50,145),20)
    c3.draw(win)
    c3.setFill("white")
    c3.setOutline("white")

 
    r1 = Rectangle(Point(30,160),Point(70,165))
    r1.draw(win)
    r1.setFill("black")

    r2 = Rectangle(Point(40,165),Point(60,185))
    r2.draw(win)
    r2.setFill("black")

  
    e1 = Circle(Point(42.5,150),2.5)
    e1.draw(win)
    e1.setFill("black")

    e2 = Circle(Point(57.5,150),2.5)
    e2.draw(win)
    e2.setFill("black")

 
    n = Polygon(Point(50,142.5),Point(50,137.5),Point(57.5,140))
    n.draw(win)
    n.setOutline("orange")
    n.setFill("orange")

   
    m1 = Circle(Point(40,135),1)
    m1.draw(win)
    m1.setFill("black")

    m2 = Circle(Point(45,130),1)
    m2.draw(win)
    m2.setFill("black")

    m3 = Circle(Point(50,127.5),1)
    m3.draw(win)
    m3.setFill("black")

    m4 = Circle(Point(55,130),1)
    m4.draw(win)
    m4.setFill("black")

    m5 = Circle(Point(60,135),1)
    m5.draw(win)
    m5.setFill("black")

   
    b1 = Circle(Point(50,115),3)
    b1.draw(win)
    b1.setFill("black")

    b2 = Circle(Point(50,105),3)
    b2.draw(win)
    b2.setFill("black")

    b3 = Circle(Point(50,95),3)
    b3.draw(win)
    b3.setFill("black")

   
    rect1 = Rectangle(Point(140,0),Point(160,25))
    rect1.draw(win)
    rect1.setOutline("brown")
    rect1.setFill("brown")
    
    t1 = Polygon(Point(100,25),Point(200,25),Point(150,65))
    t1.draw(win)
    t1.setOutline("forest green")
    t1.setFill("forest green")

    t2 = Polygon(Point(110,60),Point(190,60),Point(150,100))
    t2.draw(win)
    t2.setOutline("forest green")
    t2.setFill("forest green")

    t3 = Polygon(Point(120,90),Point(180,90),Point(150,120))
    t3.draw(win)
    t3.setOutline("forest green")
    t3.setFill("forest green")

    t4 = Polygon(Point(130,115),Point(170,115),Point(150,135))
    t4.draw(win)
    t4.setOutline("forest green")
    t4.setFill("forest green")

    t5 = Polygon(Point(135,132.5),Point(165,132.5),Point(150,155))
    t5.draw(win)
    t5.setOutline("forest green")
    t5.setFill("forest green")


    n = Polygon(Point(150,152.5),Point(147.5,160),Point(140,162.5),Point(147.5,165),Point(150,172.5),Point(152.5,165),Point(160,162.5),Point(152.5,160))
    n.draw(win)
    n.setOutline("gold")
    n.setFill("gold")

    
    o1 = Circle(Point(150,142.5),2.5)
    o1.draw(win)
    o1.setOutline("red")
    o1.setFill("gold")

    o2 = Circle(Point(135,115),2.5)
    o2.draw(win)
    o2.setOutline("red")
    o2.setFill("gold")

    o3 = Circle(Point(165,115),2.5)
    o3.draw(win)
    o3.setOutline("red")
    o3.setFill("gold")

    o4 = Circle(Point(150,95),2.5)
    o4.draw(win)
    o4.setOutline("red")
    o4.setFill("gold")

    o5 = Circle(Point(135,75),2.5)
    o5.draw(win)
    o5.setOutline("red")
    o5.setFill("gold")

    o6 = Circle(Point(165,75),2.5)
    o6.draw(win)
    o6.setOutline("red")
    o6.setFill("gold")

    o7 = Circle(Point(115,60),2.5)
    o7.draw(win)
    o7.setOutline("red")
    o7.setFill("gold")

    o8 = Circle(Point(185,60),2.5)
    o8.draw(win)
    o8.setOutline("red")
    o8.setFill("gold")

    o9 = Circle(Point(150,30),2.5)
    o9.draw(win)
    o9.setOutline("red")
    o9.setFill("gold")

    
    d1 = Polygon(Point(140,135),Point(142.5,132.5),Point(140,130),Point(137.5,132.5))
    d1.draw(win)
    d1.setOutline("gold")
    d1.setFill("red")

    d2 = Polygon(Point(160,135),Point(162.5,132.5),Point(160,130),Point(157.5,132.5))
    d2.draw(win)
    d2.setOutline("gold")
    d2.setFill("red")

    d3 = Polygon(Point(150,122.5),Point(152.5,120),Point(150,117.5),Point(147.5,120))
    d3.draw(win)
    d3.setOutline("gold")
    d3.setFill("red")

    d4 = Polygon(Point(125,92.5),Point(127.5,90),Point(125,87.5),Point(122.5,90))
    d4.draw(win)
    d4.setOutline("gold")
    d4.setFill("red")

    d5 = Polygon(Point(175,92.5),Point(177.5,90),Point(175,87.5),Point(172.5,90))
    d5.draw(win)
    d5.setOutline("gold")
    d5.setFill("red")

    d6 = Polygon(Point(150,67.5),Point(152.5,65),Point(150,62.5),Point(147.5,65))
    d6.draw(win)
    d6.setOutline("gold")
    d6.setFill("red")

    d7 = Polygon(Point(130,47.5),Point(132.5,45),Point(130,42.5),Point(127.5,45))
    d7.draw(win)
    d7.setOutline("gold")
    d7.setFill("red")

    d8 = Polygon(Point(170,47.5),Point(172.5,45),Point(170,42.5),Point(167.5,45))
    d8.draw(win)
    d8.setOutline("gold")
    d8.setFill("red")

    d9 = Polygon(Point(105,27.5),Point(107.5,25),Point(105,22.5),Point(102.5,25))
    d9.draw(win)
    d9.setOutline("gold")
    d9.setFill("red")

    d10 = Polygon(Point(195,27.5),Point(197.5,25),Point(195,22.5),Point(192.5,25))
    d10.draw(win)
    d10.setOutline("gold")
    d10.setFill("red")

    win.getMouse()
    win.close()
    
main()
    
