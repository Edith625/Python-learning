def wrapper(fn): #装饰谁传谁,fn就是add
      def inner(): #内层函数调用
            print("被装饰函数执行之前")
            fn() #执行被装饰函数
            print("被装饰函数执行之后")
      return inner #内层函数返回
def add():
      print("我是新增函数")
# a = wrapper(add) #add作为参数传递 a就是inner
add = wrapper(add) #add变成inner
# a() #执行inner函数
add() #执行inner函数 

# 语法糖
def wrapper(fn):
      def inner():
            print("执行目标函数之前")
            fn()
            print("执行目标函数之后")
      return inner
@wrapper # add=wrapper(add)
def add():
      print("我叫add")
add()
print(add)
