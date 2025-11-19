# lst = ["hello", "fine", "nice"]
# it = lst.__iter__() #迭代器interator
# print(dir(it))

# ret = it.__next__()#下一个
# print(ret)

# ret = it.__next__()
# print(ret)

# ret = it.__next__()
# print(ret)

# ret = it.__next__()
# print(ret) #StopIteration


# s = {"hello", "dadada", "dedede"}
# it = s.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

#使用iter（）获取迭代器
# lst = [11,22,33]
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))


# for循环内部大致的工作机制
lst = ["张无忌", "谢广坤", "张乘乘"]
it = lst.__iter__() #拿到迭代器
while True:
      try: #尝试下面代码
            obj = it.__next__() #拿到数据
            print(obj)
      except StopIteration: #如果出现stopiteration，开始执行代码
            break #结束循环