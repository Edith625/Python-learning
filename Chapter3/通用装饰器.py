# def wrapper(fn):
#       def inner():
#             print("开挂")
#             fn()
#             print("关闭外挂")
#       return inner
# @wrapper
# def dnf():
#       print("我要玩DNF")
# dnf()


# 如果被装饰有参数
def wrapper(fn):
      def inner(username, password):
            print("开挂")
            fn(username, password) #执行目标函数
            print("关闭外挂")
      return inner
@wrapper
def dnf(username, password):
      print(f'enter name为{username}, {password } 我要玩DNF')
dnf("admin", "123456") #执行inner