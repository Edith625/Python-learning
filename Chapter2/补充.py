# 循环删除列表数据
lst = ["张无忌", "张翠山", "张三丰", "张无暇"]
# 删除姓张的人
# for name in lst:
#     if name.startswith('张'):
#         lst.remove(name)
# print(lst)
# 相当于错开数据

# new_lst = []删除
# for name in lst:
#     if name.startswith('张'):
#         new_lst.append(name)
# for a in new_lst:
#     lst.remove(a)
# print(lst)

# new_lst = []
# for name in lst[:]:
#     if name.startswith("张"):
#         lst.remove(name)
# print(lst)

# 字典
# dic = {"jay": "周杰伦", "55k": "卢本伟"}
# lst = list(dic.keys())
# for k in lst:
#       dic.pop(k)
# print(dic)

# a = [10, 20, 30]
# b = [10, 20, 30]
# print(a == b) #判断内容值是否一致
# print(a is b) #判断两个内容内存地址是否一致
# is用来判空，内存地址是否一致

# while循环
# i = 0
# while i < 10:
#       print(i)
#       i += 1
# else:
#       print("ok")

# i = 0
# while i < 10:
#       if i == 8:
#             break #结束循环
#       print(i)
#       i += 1
# else: #条件不成立默认执行
