# s = "sylar"

# s1 = s.center(10) #强行拉长几个单位，原来字符串在中间
# print(s1)

# strip()#默认去掉字符串左右两边的空白(空格, \t,\n)

# username = input("please enter your name").strip()
# password = input("please enter your password").strip()
# if username == 'admin' and password == '123':
#     print("loading success")
# else:
#     print("loading unsuccess")

# s = "sb_admin_sb"
# print(s.strip("sb"))

# replace()字符串替换
# s = "i realy like eat KFC"
# s1 = s.replace("KFC", "***")
# print(s1)                  

# s = " a    b   c   "
# s1 = s.replace(" ", "")
# print(s1)

# s = "a_b_c_d" #字符串切割
# lst = s.split("_") #_下划线切割
# print(lst)

# join() #把一个列表组合成一个字符串
lst = ['a','b','c','d']
s = "_love_".join(lst)
print(s)

