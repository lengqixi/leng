# a = (1,2,3,4,"haha","哈哈哈","呼呼呼",True)
# # print(a[5])
# # print(a.index("呼呼呼"))
# # print(a.count("haha"))
# # b = (a,"哈哈","嘻嘻")
# # print(b[0][4])  
# print(a[0:3])
# print(a[3:6])
# print(a[6:])
a = [1,2,3,4,"haha","哈哈哈1","呼呼呼",True]
a.append("append1")
a.append("append2")
# print(a)
a.insert(0,"insert")
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
a = {}
X = {}
Y = {}
b = 1
while b <= 3:
    a.update(name=input("姓名："),mark=input("分数："))
    b = b+1
    mark = int(a.get("mark"))
    # mark = int(mark)
    name = a.get("name")
    if mark >= 60:
        X[name] = mark

        # X.append(h)
    else:
        Y[name] = mark

print("及格：",X)
print("不及格：",Y)
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