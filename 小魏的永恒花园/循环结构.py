#循环结构
#while循环
i = 0
while i<6:
	print(i)
	i+=1

print("***********")
num2 = 0
sum_all = 0 
while num2<=100:
	sum_all = sum_all+num2
	num2+=1
	
print(sum_all)
print("****************")


#for循环
for x in (10,20,30):
	print(x)

d = {"name":"高旗","age":18,"job":"程序员"}
for x in d:
	print(x)
for x in d.keys():
	print(x)
for x in d.values():
	print(x)
for x in d.items():
	print(x)
	
print("*********")
sum_all = 0
sum_even = 0
sum_odd = 0
for x in range(101):
	sum_all += x
	if x%2 == 0:
		sum_even+=x
	else:
		sum_odd+=x
print(sum_all)
print(sum_even)
print(sum_odd)

#嵌套循环
for x in range(5):
	print(x)
	for y in range(5):
		print(x%2,end = '\t')
		print(x%2,end = '\t')

print()		
#
print("*************")
for m in range(1,10):
	for n in range(m+1):
		print("{0}*{1}={2}".format(n,m,(n*m)),end = "\t")
	print() #换行

print("***************")



	
	
	
	
	
	
	
	
	
	
