import turtle as t
import math

x1,y1=100,100
x2,y2=100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

t.penup()
t.goto(x1,y1)
t.pendown()

t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x4,y4)

dis = math.sqrt((x1-x2)**2+(x3-x4)**2)
t.write(dis)

a  = (3==4)
print(a)


 





