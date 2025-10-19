# 输入一个名字判断是不是a开头
# startwith() 判断是不是以XXX开头
# name = input("please enter your name:")
# if name.startswith("a"):
#     print("yes")
# else:
#     print("no")

# endswith()判断是不是以XXX结尾
# s = "the weather is good"
# print(s.endswith("weather"))
# print(s.endswith("good"))

# s.count("") 计算字符串中有多少个XXX
# s = "python_java_php_ajax"
# print(s.count("s"))

# s = "i realy like python"
# s1 = "我最喜欢python了"
# print(s.find("b")) #查找字符串，查找到返回索引，查找不到返回-1
# print(s1.find("哈"))

s = "我最喜欢python"
print(s.index("python")) #查找字符串返回索引
print(s.index("#")) # 找不到报错
