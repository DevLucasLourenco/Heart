import turtle
import os 

pen = turtle.Turtle()


def curvar():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def coracao():
    
    pen.fillcolor('red')
    pen.begin_fill()
    
    pen.left(140)
    pen.forward(113)
    
    curvar()
    pen.left(120)
    
    curvar()
    
    pen.forward(112)
    
    pen.end_fill()
    
    
def txt():
    pen.up()
    pen.setpos(-140,65)
    pen.down()
    pen.color('white')
    
    pen.write( '''
                20 Ligações -
              Baco Exu do Blues
                        01:42
              ''', font=('Verdana',12,'bold'))

   
    
coracao()
txt()
pen.ht()
        
os.system('pause')