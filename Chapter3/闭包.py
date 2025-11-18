# def func(): #本质和变量没什么区别
#       print("hehe")

# # func = 20
# a = func
# print(a)
# print(func)

# def func1():
#       print("hellow")
# def func2():
#       print("hellow1")
# def func3():
#       print("hellow2")

# lst = [func1, func2, func3]#可以当变量使用，调用+（） 
# for item in lst:
#       item()
#       print(item)

# def func1():
#       print("hellow")

# def func2():
#       print("nice")

# def func3():
#       print("fine")

# def handle(*fn): #作为参数传递
#      for item in fn:
#       item()
# handle(func1, func2, func3)

# def func():
#      def func2():
#           print("i am func2")
#           return func2 #作为返回值
# fn = func()
# fn()

# 闭包

def func():
      a = 10 #局部变量，无法修改
      def inner():
            print(a)
      return inner
fn = func()
fn() #fn是inner，在函数外部访问到了局部变量
# 作用1:变量封锁，外界只能看不能修改
# 作业2: 变量常驻内存