import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle(x,y):
    'ฟังก์ชันนี้เอาไว้วาดรูปสี่เหลี่่ยม'
    for i in range(4):
        tao.forward(x)
        tao.left(y)

def Triangle(x,y):
    for i in range(1):
        tao.forward(x)
        tao.left(y)
        tao.forward(x)
        tao.left(y)
        tao.forward(x)

def roof(x,y):
    for i in range(3):        
        if(i == 2):
            tao.left(x/i)
            tao.forward(y)
            break
        tao.left(x)
        tao.forward(y)
        print(i)
        
        

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(50,50)
Rectangle(100,90)
Go(50,150)
Triangle(100,120)
Go(150,150)
roof(120,100)
Go(250,150)
Rectangle(100,90)
Go(125,100)
Rectangle(50,90)

