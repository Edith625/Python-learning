# def func():
#       print("123")
#       yield "hi" #生成器函数 yield也有返回的意思(调用next)
# gen = func()
# print(gen) #<generator object func at 0x100c30a00>
# # 生成器函数，在生成器函数执行时创建生成器
# ret = gen.__next__() #返回值
# print(ret) 

# def func():
#       print("11")
#       yield "hi" 
#       print("22")
#       yield "hellow" 
#       print("33")
#       yield "nice" 

# gen = func()
# print(gen) 

# ret1 = gen.__next__() #返回值
# print("接收到的数据是", ret1) 

# ret2 = gen.__next__() #返回值
# print("接收到的数据是", ret2) 

# ret3 = gen.__next__() #返回值
# print("接收到的数据是", ret3) 

# ret4 = gen.__next__() #返回值
# print("接收到的数据是", ret4)  #StopIteration报错



# 生成器节省内存
# def order():
#       for i in range(10000):
#             yield f"clothes{i}"
# g = order()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

#改进
def order():
      lst = []
      for i in range(10000):
            lst.append(f"clothes{i}")
            if len(lst) == 50:
                  yield lst
                  lst = []
g = order()
print(g.__next__())
print(g.__next__())

