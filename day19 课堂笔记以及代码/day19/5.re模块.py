import re
# ret = re.findall('\d+','19740ash93010uru')
# print(ret)
#
# ret = re.search('\d+','19740ash93010uru')
# print(ret)  # 变量
# if ret:
#     print(ret.group())

# 预习一个现象并且找到答案 - 分组有关系()
ret = re.findall('9(\d)\d','19740ash93010uru')
print(ret)
#
ret = re.search('9(\d)(\d)','19740ash93010uru')
print(ret)  # 变量
if ret:
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))