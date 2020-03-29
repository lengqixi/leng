# a = (1,2,3,4,"haha","哈哈哈","呼呼呼",True)
# # print(a[5])
# # print(a.index("呼呼呼"))
# # print(a.count("haha"))
# # b = (a,"哈哈","嘻嘻")
# # print(b[0][4])  
# print(a[0:3])
# print(a[3:6])
# print(a[6:])
# a = [1,2,3,4,"haha","哈哈哈1","呼呼呼",True]
# a.append("append1")
# a.append("append2")
# # print(a)
# a.insert(0,"insert")
# print(a)
# b = a.pop(6)
# print(b)
# xx = ["你好","你挺好"]
# a.extend(xx)
# print(a)
# print(a.count(1))
# a = {"name":"小老弟","age":25,"sex":"男"}
# print(a)
# print(a["age"])
# a["high"] = 188
# a["name"] = "老弟咋回事"
# print(a)
# a = {"name":input("请输入姓名:"),"age":input("请输入年龄："),"sex":input("请输入性别:")}
# a.update(name="老弟")
# print(a.get("name"))
# age = int(input("请输入年龄："))
# if age <= 20:
#     print("小学生")
# elif age <= 30:
#     print("老弟")
# elif age <= 60:
#     print("大哥")
# else:
#     print("小老头")
# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789":
#     a = int(a)
#     print("年龄为:",a)

# else:
#     print("请输入正确年龄！")
# b = type(a)
# if b is int:
#     print("大数字")
# elif b is str:
#     print("文字")
# else:
#     print("不是人")
# a = 18
# while a < 20:
#     print("哈哈哈",a)
#     a = a+1
# a = {}
# X = {}
# Y = {}
# b = 1
# while b <= 3:
#     a.update(name=input("姓名："),mark=input("分数："))
#     b = b+1
#     mark = int(a.get("mark"))
#     # mark = int(mark)
#     name = a.get("name")
#     if mark >= 60:
#         X[name] = mark

#         # X.append(h)
#     else:
#         Y[name] = mark

# print("及格：",X)
# print("不及格：",Y)
# a = {}
# a.update(name=input("姓名："),mark=input("分数："))
# a.update(name=input("姓名："),mark=input("分数："))
# print(a)
# a = []
# b = {"name":"xx"}
# c = {"name":"ahha"}
# a.append(b)
# a.append(c)
# # a.append(2)
# print(a)
# b.update(name="qqq")
# a.append(b)
# print(a)
# for i in range(100):
#     print(i)
# a = list(range(0,100,2))
# print(a)
# for i in range(10):
#  print(i)
# a = ["haha","老李","小王姐","老王"]
# for i in a:
#     print(i)
# a = list(range(10))
# print(a,end="---")
# print(10)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="   ")
#     print()
# a = 10
# while a < 20:

#     for r in range(0,30):
#         print("红灯还有",(30-r),"秒结束")
#     for g in range(0,35):
#         print("绿灯还有",(35-g),"秒结束")
#     for y in range(0,3):
#         print("黄灯还有",(3-y),"秒结束")
# username = input("请输入账号：")
# while len(username) < 5 or len(username) > 8:
#     print("账号长度不符格则，请重新输入！")
#     username = input("请重新输入账号：")
# password = input("请输入密码：")
# while len(password) < 6 or len(password) > 12:
#     print("不符合格则，请重新输入！")
#     password = input("请重新输入密码：")
# a = {}
# a[username] = password
# print(a)
try :
    print(a+1)
except:
    print("代码写错")