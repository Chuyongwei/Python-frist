#双向选择
s = input("输入一个数字:")
if(int(s)<10):
	print(s)
else:
	print("数字太大")

#三元分支运算: 真 if() else 假	
print(s)if(int(s)<10)else print("数字太大")

#多分支语句
score = int(input("请输入分数"))
grade = ""
if int(score) <60:
	grade = "不及格"
elif(score<=80):
	grade = "及格"
elif score<90:
	grade = "良好"
else:
	grade = "优秀"
print("成绩是：{0},等级是：{1}".format(score,grade))

print("*****************")
if score <60:
	grade = "不及格"
if 60<=score<80:
	grade = "及格"
if 80<=score<90:
	grade = "良好"
if score>=90:
	grade = "优秀"
print("成绩是：{0},等级是：{1}".format(score,grade))

#选择结构的嵌套
score = int(input("请输入分数"))
if score>100 or score<0:
	score = int(input("输入错误！请重新输入在0——100之间的数"))
else:
	if score>=90:
		grade = 'A'
	elif score>=80:
		grade = 'B'
	elif score>=70:
		grade = 'C'
	elif score>=60:
		grade = 'D'
	print(grade)
	
	
print("***************")
score = int(input("请输入分数"))
degree = "ABCDE"
if score>100 or score<0:
	score = int(input("输入错误！请重新输入在0——100之间的数"))
else:
	num = score//10
	if num<6:
		grade = 5
	print("分数是{0},等级是：{1}".format(score,degree[9-num]))
	
#死循环处理