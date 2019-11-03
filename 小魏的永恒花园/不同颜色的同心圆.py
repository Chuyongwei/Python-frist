import turtle

t = turtle.Pen()

my_colors = ('red','yellow','green','black')
t.speed(0)

for i in range(50):
	t.penup()
	print(i)
	t.color(my_colors[i%len(my_colors)])
	t.goto(0,-10*i)
	
	t.pendown()
	t.circle(10*i)
	
	
	
	
turtle.done()