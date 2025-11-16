# 形参：函数声明位置编写的变量
# 位置参数 从左到右编写
# 默认值参数

# def func(name, age, gender='male'):
#       print("enter name", name)
#       print("enter age", age)
#       print("enter gender", gender)
# func("周杰伦", 18, 'male')
# func("周杰", 22, 'male')
# func("周伦", 16, 'male')
# func("周星驰", 19, 'male')
# func("周啊伦", 20, 'male')
# func("蔡依林", 18, 'female')

def func(val, lst=[]):
      lst.append(val)
      print(lst)
func(10086)
func(10010) #[]为可变数据，会共享
func(777888, [])
