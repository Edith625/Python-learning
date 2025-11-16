# * 动态传参：给出多个参数，在形参位置一次性接受,自动生成元组
# def chi(*food):
#       print(food)
# chi("noodle")
# chi("chiken", "buger")
# chi("rice", "potato", "tomato") 按位置参数

# 按关键词参数 自动生成字典
# def chi(**food):
#       print(food)
# chi(main_food="noodle", fu_food="chiken")

# 位置参数 arges 默认参数 kwargs 一定按照这个顺序
def func(*arges, **kwargs): #可以接受任意函数
      print(arges)
      print(kwargs)
func("hello", "fine", a="haha", b="hehe")