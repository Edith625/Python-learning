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


# # 如果被装饰有参数
# def wrapper(fn):
#       def inner(*args, **kwargs):#含有参数的函数时使用
#             print("开挂")
#             fn(*args, **kwargs) #执行目标函数
#             print("关闭外挂")
#       return inner
# # @wrapper
# # def dnf(username, password):
# #       print(f'enter name为{username}, {password } 我要玩DNF')
# # dnf("admin", "123456") #执行inner

# @wrapper
# def wz(wx):
#       print(f"使用账户{wx}登陆王者荣耀")
# wz("大佬")

# 目标函数有返回值
# def wrapper(fn):
#       def inner():
#             print("开挂")
#             ret = fn()
#             print("关闭外挂")
#             return ret
#       return inner
# @wrapper
# def dnf():
#       print("我要玩DNF")
#       return "123456"
# ret = dnf()
# print("我得到了", ret)

# 通用装饰器写法
# def wrapper(fn): # wrapper可替换
#       def inner(*args, **kwargs):
#             #执行目标函数之前
#             ret = fn(*args, **kwargs)
#             #执行目标函数后
#             return ret
#       return inner
# @wrapper
# def target():
#       pass
# target()



# flag = False

# def login_vertify(fn): # wrapper可替换
#       def inner(*args, **kwargs):
#             while True:
#                   if flag: #执行目标函数之前 
#                         ret = fn(*args, **kwargs)#执行目标函数后
#                         return ret
#             else:
#                   login()
#       return inner

# def login():
#       global flag
#       username = input("please enter username: ")
#       password = input("please enter password: ")
#       if username == 'admin' and password == "123456":
#             flag = True
#             print("login success")
#       else:
#             print("incorrect")
# @login_vertify
# def add():
#       print("执行新增操作")
# @login_vertify
# def upd():
#       print("执行修改操作")
# add()
# add()
# upd()
# upd()


flag = False

def login():
    global flag
    username = input("please enter username: ")
    password = input("please enter password: ")
    if username == 'admin' and password == "123456":
        flag = True
        print("login success")
    else:
        print("incorrect")

def login_vertify(fn):
    def inner(*args, **kwargs):
        global flag
        # 如果没登录，先去登录
        while not flag:
            login()
        # 登录成功后再执行真正的函数
        return fn(*args, **kwargs)
    return inner
@login_vertify
def add():
    print("执行新增操作")

@login_vertify
def upd():
    print("执行修改操作")

add()
add()
