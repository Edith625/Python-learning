# lst = ["张无忌", "赵敏", "成昆","金毛狮王"]
# print(lst[-2])
# print(lst[1:2:2])

# lst新增
# lst = ["a", "b"]
# lst.append("c") # 新增
# print(lst)

#lst插入
# lst = ["a", "b"]
# lst.insert(1, "c")
# print(lst)

#lst迭代新增
# lst = ["a", "b"]
# n = ["c", "d","e"]
# lst.extend(n)
# print(lst)

#lst删除
# lst = ["a", "b","c","d"]
# lst.remove("a") #删除某个元素
# print(lst)

lst = ["a", "b", "c", "d"]
# item = lst.pop() #弹出最后一个
# print(lst)
# print(item)
# item = lst.pop(1)#指定位置删除
# print(lst)

# del lst[2]
# print(lst)

# lst.clear()#清空
# print(lst)

#修改
# lst = ["aa","cc"]
# lst[1] = "bb"
# print(lst)

#查询
# lst = ["a", "b", "c", "d","e"]
# for item in lst:
#     print(item)

# i = 0
# while i < len(lst):
#     item = lst[i]
#     print(item)
#     print(i)
#     i +=1

#for循环数数
# for i in range (10):
#     print(i)

#for循环拿到索引和切片
# for i in range (len(lst)):
#     print(i)
#     print(lst[i])

lst = ["谢广坤", "刘能",["雪碧", ["王思聪", "王健林", "马云"], "芬达", "可乐", 100], "常规"]
print(lst[2][1][2])
# 林改成a
lst[2][1][1] = lst[2][1][1].replace("林", "a")
print(lst)

# 100*10
lst[2][4]*=10
print(lst)