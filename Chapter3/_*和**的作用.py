# def func(*args):
#       print(args)
# lst = ["张无忌", "张翠山", "张三丰"]

# func(lst[0], lst[1], lst[2])
# # 列表中的每一项当作参数传递给函数

# # 借助*打散操作
# func(*lst) #借用*将列表打散成位置参数传递进去

def func(**kwargs):
      print(kwargs)
dic = {"name": "赵敏", "age": 18}
func(name=dic['name'], age=dic['age'])
func(**dic) #把字典转化为关键字参数