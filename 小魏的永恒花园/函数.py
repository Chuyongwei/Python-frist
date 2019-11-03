#函数的用法
def test1():
	print("*"*10)
	print("4"*10)
	
def test2(a,b=0):
	'''用于比较字符'''
	c = '''
		ksladj;float
		sklfa
		slkajf
		'''
	print(c)
	if(a>b):
		print(a,"较大值")
	else:
		print(b,"jiaodazh")
		
		
test2(0,10)
help(test2.__doc__)

print("*****************")
#带有返回值的参数
def add(a,b):
	print("计算两个数的和：{0}+{1}={2}".format(a,b,a+b))
	return a+b
	

c = add(4,5)
print(c)

#函数也是对象
print("*********")
def test4():
	print("tttt")
test4()
c = test4
c()

#全局变量和局部变量
print("***********")
a = 3     #全局变量

def test01 ():
	b = 4		#局部变量
	print(b*10)
test01()	
print(a)

print("************")
#传递不可变对象
a = 100 
def tran(n):
	print("n:",id(n))
	n = n+200
	print("n:",id(n))
	print(n)
	
tran(a)
print("a",id(a))

#浅拷贝和深拷贝
print("*&***************")
import copy
def textcopy():
	'''测试浅拷贝'''
	a = [10,20,[5,6]]
	b = copy.copy(a)
	
	print("a",a)
	print("b",b)
	
	b.append(30)
	b[2].append(7)
	print("浅拷贝...")
	print("a:",a)
	print("b:",b)
	
textcopy()

def textcopy2():
	'''测试深拷贝'''
	a = [10,20,[5,6]]
	b = copy.deepcopy(a)
	
	print("a",a)
	print("b",b)
	
	b.append(30)
	b[2].append(7)
	print("深拷贝...")
	print("a:",a)
	print("b:",b)
textcopy2()

#传递不可变对象时，不可变对象里面包含的子对象是可变的，则方法内修改了这个可变对象，愿对象也发生了变化
print("***************")
a = 0
print("a",id(a))

def test01(m):
	print("m:",id(m))
	m = 20 
	print(m)
	print("m:",id(m))
	
test01(a)

print("***************")
#默认参数

def f1(a,b,c,d):
	print("{0}-{1}-{2}-{3}".format(a,b,c,d))
def f2(a,b,c=9,d=0):
	print("{0}-{1}-{2}-{3}".format(a,b,c,d))
f1(2,3,4,5)
f2(9,5)

#可变参数
#*:将多个参数收集到一个“元组”对象中
#**：将多个参数收集到一个“字典”对象中
def f2(a,b,*c):
	print(a,b,c)

f2(8,9,20,4,34,4)

def f3(a,b,**c):
	print(a,b,c)
	
f3(8,9,name = 'gaoqi',age = 18)
#‘*’后面的参数使用时应标记
def f4(*a,b,c):
	print(a,b,c)
	
f4(3,c = 5,b = 4)


print("*******************")

#lambda 表达式
f = lambda a,b,c,d:a*b*c*d

def test5(a,b,c,d):
	sprint("######")
	return a*b*c*d

print(f(2,3,4,5))

g = [lambda a:a*2,lambda b:b*3]

print(g[0](6),g[1](4))