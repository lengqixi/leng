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
a = {"name":"小老弟","age":25,"sex":"男"}
print(a)
print(a["age"])
a["high"] = 188
a["name"] = "老弟咋回事"
print(a)