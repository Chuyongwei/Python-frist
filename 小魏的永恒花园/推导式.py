#推导式

p = [x for x in range(10)]
print(p)


cells = [(row,col) for row in range(1,10) for col in range(1,10)]
for cell in cells:
	print(cell)
	
#字典推导式
my_text = "I love you,i love sxt,i love gaoqi"
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

#集合推导式

#迭代器推导式
ant = (x for x in range(1,20))
print(tuple(ant))