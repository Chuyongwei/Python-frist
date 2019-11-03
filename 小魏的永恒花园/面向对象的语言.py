#C语言的结构体
'''	
struct resume{
	int age
	char name[10]
}
'''
'''
	结构体记录数据
	对象不仅可以记录数据，还可以记录方法（函数）
'''
#类分方法和状态
class Student:
	company = "尚学堂" #类属性
	count = 0 #类属性
	def __init__(self,name,score):#构造函数双下划线,初始化创建好对象
		self.name = name#实例属性
		#self.__name = name #私有属性
		self.score = score
		Student.count = Student.count+1
	def say_score(self):#第一个参数必须是self
		print("{0}的分数是：{1}".format(self.name,self.score))
	def __del__(self):
		print("销毁{0}",self.name)
	
def say_score(self): #实例方法
		print("我的公司是：",Student.company)
		print(self.name,'的分数是：',self.score)	

s1 = Student("高崎",18)
s1.say_score()

s1.age = 32
s1.salsry = 3000
#del s1
print(s1.salsry)

s2 = Student("高嘻嘻",18)   
s2.say_score()
Student.say_score(s2)#本质就是Student.say_score(self) 

print(dir(s2))
print(s2.__dict__)#对象的属性字典

#print(isinstance(s2,Man))
		
s3 = Student("高嘻",18)   #s1 是实例对象，自动调用__init__()方法
s3.say_score()
print("一共创建{0}个对象".format(Student.count))

print("*********************")
#类属性
'''
class Student1:
	@classmethod#类方法
	@staticmethod#静态方法
'''
#测试__call__，可调用对象

class SalaryAccount: 
	'''工资计算类''' 
	def __call__(self, salary):
		yearSalary = salary*12
		daySalary = salary//30
		hourSalary = daySalary//8
		return dict(monthSalary=salary,yearSalary=yearSalary,daySalary=daySalary,hourSalary=hourSalary)#字典
s = SalaryAccount()
print(s(5000)) 
#方法没有重载

'''
私有属性和私有方法:在名字前加双下划线(__name)，访问用_Emploee(__name)
	