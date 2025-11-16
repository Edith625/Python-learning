# def yue(tools, gender): #形参，创建的信息-变量
#       print("1. 打开手机")
#       print(f"2. 打开{tools}")
#       print(f"3. 找{gender}")
#       print("4. 约")
# yue("陌陌", "男的") #希望是陌陌 实参-给函数传递的信息，调动函数传递的信息,传递具体的值
# yue("探探", "女的") #希望是探探

# 位置参数-实参-按照位置给形参传递数据
# def func(a, b, c):
#       print(a, b, c)
# func(11,22,33)

# 关键字参数,按照形参名字进行传递数据
# def func(a, b, c):
#       print(a, b, c)
# func(b=99, c=56, a=88)

# 混合参数(位置+关键字)
# def func(a, b, c):
#       print(a, b, c)
# func(11, c=99, b=22)

# 形餐在执行的时候必须有明确的数据，否则报错
def func(a, b, c):
      print(a, b, c)
func(11, 22) #实惨数量与形参一致